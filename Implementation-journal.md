# IMPLEMENTATION JOURNAL - Employee Registration Form

## Submitted By:
**Antariksha Rawat**  

## Submitted To:
**Mr. Vipin Tripathi**  

## Test Case Version:

## Reviewer Name:
**Mr. Vipin Tripathi**

---

## **Goal**
This document explains how to pull the project from GitHub and run it on a local machine, ensuring all required dependencies and configurations are met. The project involves using **Flask** in the backend, **PostgreSQL** as the database, and **Valkey** for key-value storage.

---

## **Table of Contents**
### **1. Hardware Requirements**
- **Processor**: Intel Core i5/i7 (or AMD equivalent)
- **RAM**: Minimum 8GB (16GB recommended for better performance)
- **Storage**: At least 20GB of free space
- **Network**: Stable internet connection

### **2. Software Requirements**
- **Operating System**: Ubuntu (or any Linux-based OS)
- **Programming Language**: Python 3.10+
- **Database**: PostgreSQL
- **Cache Storage**: Valkey
- **Containerization**: Podman
- **Virtual Environment**: Python venv

#### **Required Packages**
- Flask (for backend)
- psycopg2 (for PostgreSQL connectivity)
- redis (for Valkey connection)

### **3. Network Requirements**
- **Ports to be Opened**:
  - 5432 (PostgreSQL)
  - 6379 (Valkey)
  - 5000 (Flask backend)
- **Firewall Rules**: Ensure no blocking on the required ports

---

## **PREREQUISITES**

### **Hardware Requirements**
- Minimum **4GB RAM** (8GB recommended)
- At least **10GB of free disk space**

### **Software Requirements**
- **Operating System**: Ubuntu (or any Linux-based OS)
- **Dependencies**:
  - Git
  - Docker & Podman
  - Python (Ensure Flask is installed)
  - PostgreSQL
  - Valkey

### **Network Requirements**
- **Active internet connection** for pulling the repository and installing dependencies

---

## **STEPS**

### **STEP 1: Clone the Repository**

Command executed:
```sh 
git clone https://github.com/Antar365/Flask_postgres_valkey.git
cd Flask_postgres_valkey
```
Output:
```sh
adarsh@adarsh:~$ git clone https://github.com/Antar365/Flask_postgres_valkey.git
cd Flask_postgres_valkey
Cloning into 'Flask_postgres_valkey'...
remote: Enumerating objects: 2019, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 2019 (delta 2), reused 0 (delta 0), pack-reused 2013 (from 1)
Receiving objects: 100% (2019/2019), 42.22 MiB | 10.53 MiB/s, done.
Resolving deltas: 100% (118/118), done.

```

Verify it is deployed:
```sh 
Run: ls
```

---

### **STEP 2: Set Up the Environment**

Command executed:
```sh 
sudo apt install python3.12-venv
```

Output: 
```sh
adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install python3.12-venv
[sudo] password for adarsh: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-pip-whl python3-setuptools-whl
The following NEW packages will be installed:
  python3-pip-whl python3-setuptools-whl python3.12-venv
0 upgraded, 3 newly installed, 0 to remove and 52 not upgraded.
Need to get 2,424 kB of archives.
After this operation, 2,771 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-pip-whl all 24.0+dfsg-1ubuntu1.1 [1,703 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-setuptools-whl all 68.1.2-2ubuntu1.1 [716 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3.12-venv amd64 3.12.3-1ubuntu0.4 [5,676 B]
Fetched 2,424 kB in 3s (714 kB/s)           
Selecting previously unselected package python3-pip-whl.
(Reading database ... 236912 files and directories currently installed.)
Preparing to unpack .../python3-pip-whl_24.0+dfsg-1ubuntu1.1_all.deb ...
Unpacking python3-pip-whl (24.0+dfsg-1ubuntu1.1) ...
Selecting previously unselected package python3-setuptools-whl.
Preparing to unpack .../python3-setuptools-whl_68.1.2-2ubuntu1.1_all.deb ...
Unpacking python3-setuptools-whl (68.1.2-2ubuntu1.1) ...
Selecting previously unselected package python3.12-venv.
Preparing to unpack .../python3.12-venv_3.12.3-1ubuntu0.4_amd64.deb ...
Unpacking python3.12-venv (3.12.3-1ubuntu0.4) ...
Setting up python3-setuptools-whl (68.1.2-2ubuntu1.1) ...
Setting up python3-pip-whl (24.0+dfsg-1ubuntu1.1) ...
Setting up python3.12-venv (3.12.3-1ubuntu0.4) ...
```
Create Virtual Environment by this command:
```sh
python3 -m venv venv
source venv/bin/activate
```
Output:
```sh
adarsh@adarsh:~/Flask_postgres_valkey$ python3 -m venv venv
adarsh@adarsh:~/Flask_postgres_valkey$ source venv/bin/activate

```
Update System and Install Dependencies:
```sh 
sudo apt update
sudo apt install libpq-dev
```

Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt update
sudo apt install libpq-dev
Ign:1 https://pkg.jenkins.io/debian-stable binary/ InRelease
Hit:2 https://pkg.jenkins.io/debian-stable binary/ Release                                                                                                                        
Get:4 https://dl.google.com/linux/chrome/deb stable InRelease [1,825 B]                                                                                                           
Hit:5 http://in.archive.ubuntu.com/ubuntu noble InRelease                                                                                                           
Get:6 https://dl.google.com/linux/chrome/deb stable/main amd64 Packages [1,217 B]                                                   
Get:7 http://in.archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]                            
Get:8 http://security.ubuntu.com/ubuntu noble-security InRelease [126 kB]      
Hit:9 https://ppa.launchpadcontent.net/flexiondotorg/quickemu/ubuntu noble InRelease     
Get:10 http://in.archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]            
Get:11 http://security.ubuntu.com/ubuntu noble-security/main amd64 Packages [617 kB]
Get:12 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Packages [865 kB]
Get:13 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Components [151 kB]
Get:14 http://in.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Components [212 B]       
Get:15 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Packages [1,014 kB]
Get:16 http://security.ubuntu.com/ubuntu noble-security/main amd64 Components [8,956 B]    
Get:17 http://security.ubuntu.com/ubuntu noble-security/restricted amd64 Components [212 B]
Get:18 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Packages [803 kB]
Get:19 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Components [363 kB]          
Get:20 http://in.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Components [940 B]       
Get:21 http://in.archive.ubuntu.com/ubuntu noble-backports/main amd64 Components [208 B]
Get:22 http://in.archive.ubuntu.com/ubuntu noble-backports/restricted amd64 Components [216 B]
Get:23 http://in.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Components [17.7 kB]
Get:24 http://in.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Components [212 B]                
Get:25 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Components [51.9 kB]                   
Get:26 http://security.ubuntu.com/ubuntu noble-security/multiverse amd64 Components [212 B]
Fetched 4,276 kB in 6s (707 kB/s)                                                                                                                                                                          
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
56 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libpq5
Suggested packages:
  postgresql-doc-16
The following NEW packages will be installed:
  libpq-dev libpq5
0 upgraded, 2 newly installed, 0 to remove and 56 not upgraded.
Need to get 292 kB of archives.
After this operation, 1,031 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpq5 amd64 16.6-0ubuntu0.24.04.1 [141 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpq-dev amd64 16.6-0ubuntu0.24.04.1 [151 kB]
Fetched 292 kB in 3s (84.4 kB/s)   
Selecting previously unselected package libpq5:amd64.
(Reading database ... 236928 files and directories currently installed.)
Preparing to unpack .../libpq5_16.6-0ubuntu0.24.04.1_amd64.deb ...
Unpacking libpq5:amd64 (16.6-0ubuntu0.24.04.1) ...
Selecting previously unselected package libpq-dev.
Preparing to unpack .../libpq-dev_16.6-0ubuntu0.24.04.1_amd64.deb ...
Unpacking libpq-dev (16.6-0ubuntu0.24.04.1) ...
Setting up libpq5:amd64 (16.6-0ubuntu0.24.04.1) ...
Setting up libpq-dev (16.6-0ubuntu0.24.04.1) ...
Processing triggers for libc-bin (2.39-0ubuntu8.3) ...
Processing triggers for man-db (2.12.0-4build2) ...
```

Command Executed

```sh
sudo apt install python3.12-dev
```
Output

```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install python3.12-dev
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3.12-dev is already the newest version (3.12.3-1ubuntu0.4).
python3.12-dev set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 56 not upgraded.
```

Install Required Python Packages:
```sh
pip install -r requirements.txt
```
Output:

```sh


(venv) adarsh@adarsh:~/Flask_postgres_valkey$ pip install -r requirements.txt
Collecting Flask==3.1.0 (from -r requirements.txt (line 1))
  Using cached flask-3.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting psycopg2==2.9.10 (from -r requirements.txt (line 2))
  Using cached psycopg2-2.9.10.tar.gz (385 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting redis==5.2.1 (from -r requirements.txt (line 3))
  Using cached redis-5.2.1-py3-none-any.whl.metadata (9.1 kB)
Collecting psycopg2-binary==2.9.10 (from -r requirements.txt (line 4))
  Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
Collecting Werkzeug>=3.1 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting Jinja2>=3.1.2 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting blinker>=1.9 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->Flask==3.1.0->-r requirements.txt (line 1))
  Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
Using cached flask-3.1.0-py3-none-any.whl (102 kB)
Using cached redis-5.2.1-py3-none-any.whl (261 kB)
Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached click-8.1.8-py3-none-any.whl (98 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.5-py3-none-any.whl (134 kB)
Using cached werkzeug-3.1.3-py3-none-any.whl (224 kB)
Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23 kB)
Building wheels for collected packages: psycopg2
  Building wheel for psycopg2 (pyproject.toml) ... done
  Created wheel for psycopg2: filename=psycopg2-2.9.10-cp312-cp312-linux_x86_64.whl size=529585 sha256=03fc69a13250eddcf4abcdd4ee00b1aca36871d040d0f8df667f7ca54c4acc21
  Stored in directory: /home/adarsh/.cache/pip/wheels/ac/bb/ce/afa589c50b6004d3a06fc691e71bd09c9bd5f01e5921e5329b
Successfully built psycopg2
Installing collected packages: redis, psycopg2-binary, psycopg2, MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, Flask
Successfully installed Flask-3.1.0 Jinja2-3.1.5 MarkupSafe-3.0.2 Werkzeug-3.1.3 blinker-1.9.0 click-8.1.8 itsdangerous-2.2.0 psycopg2-2.9.10 psycopg2-binary-2.9.10 redis-5.2.1

```
Verify Flask Installation:
```sh
python3 -m flask --version
```
---

### **STEP 3: Start the Containers**

Command executed:
```sh
sudo apt install podman-compose
```

Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install podman-compose
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-dotenv
The following NEW packages will be installed:
  podman-compose python3-dotenv
0 upgraded, 2 newly installed, 0 to remove and 56 not upgraded.
Need to get 60.9 kB of archives.
After this operation, 305 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 python3-dotenv all 1.0.1-1 [22.3 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 podman-compose all 1.0.6-1 [38.6 kB]
Fetched 60.9 kB in 2s (35.6 kB/s)        
Selecting previously unselected package python3-dotenv.
(Reading database ... 237341 files and directories currently installed.)
Preparing to unpack .../python3-dotenv_1.0.1-1_all.deb ...
Unpacking python3-dotenv (1.0.1-1) ...
Selecting previously unselected package podman-compose.
Preparing to unpack .../podman-compose_1.0.6-1_all.deb ...
Unpacking podman-compose (1.0.6-1) ...
Setting up python3-dotenv (1.0.1-1) ...
Setting up podman-compose (1.0.6-1) ...
Processing triggers for man-db (2.12.0-4build2) ...


```
---

### **STEP 4: Run the Containers**

Command executed for PostgreSQL:
```sh
podman run -d --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=employee -p 5432:5432 docker.io/library/postgres
```
Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ podman run -d --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=employee -p 5432:5432 docker.io/library/postgres
Trying to pull docker.io/library/postgres:latest...
Getting image source signatures
Copying blob 4553993e7797 done   | 
Copying blob 0dc773e0cc79 done   | 
Copying blob e1ad38ab49c1 done   | 
Copying blob 20f2363da6db done   | 
Copying blob c29f5b76f736 done   | 
Copying blob 559c5c599163 done   | 
Copying blob 91393204ae54 done   | 
Copying blob c0311d3bf51b done   | 
Copying blob 931e444b6b99 done   | 
Copying blob 0de06291fc41 done   | 
Copying blob 1f9512881cf4 done   | 
Copying blob a608baae1e5c done   | 
Copying blob 91befecb86a3 done   | 
Copying blob 8da49c2b3211 done   | 
Copying config d14b06b9a9 done   | 
Writing manifest to image destination
6d2e74dd33bb6ae90e85307e7340766c9386aba58e097e40bd945bc161fb6441
```

Command executed for Valkey:
```sh 
podman run -d --name valkey_container -p 6379:6379 docker.io/valkey/valkey
```
Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ podman run -d --name valkey_container -p 6379:6379 docker.io/valkey/valkey
Trying to pull docker.io/valkey/valkey:latest...
Getting image source signatures
Copying blob c29f5b76f736 skipped: already exists  
Copying blob 4f4fb700ef54 done   | 
Copying blob e9c0e091ec2b done   | 
Copying blob 76d6b73e18e0 done   | 
Copying blob f644cba9db5c done   | 
Copying blob a0a0665da571 done   | 
Copying blob f2bf47372ada done   | 
Copying config df4420e738 done   | 
Writing manifest to image destination
1c89e30b37a9e8bcfa651d4a7dbb1128fd617c5b68f6627eac4e98f8faedc19b
```

Verify PostgreSQL is running:
```sh
podman exec -it postgres_container bash
psql -U postgres
```
---

### **STEP 5: Run the Application**

Command executed:
```sh
python app.py
```# IMPLEMENTATION JOURNAL - Employee Registration Form

## Submitted By:
**Antariksha Rawat**  

## Submitted To:
**Mr. Vipin Tripathi**  

## Test Case Version:

## Reviewer Name:
**Mr. Vipin Tripathi**

---

## **Goal**
This document explains how to pull the project from GitHub and run it on a local machine, ensuring all required dependencies and configurations are met. The project involves using **Flask** in the backend, **PostgreSQL** as the database, and **Valkey** for key-value storage.

---

## **Table of Contents**
### **1. Hardware Requirements**
- **Processor**: Intel Core i5/i7 (or AMD equivalent)
- **RAM**: Minimum 8GB (16GB recommended for better performance)
- **Storage**: At least 20GB of free space
- **Network**: Stable internet connection

### **2. Software Requirements**
- **Operating System**: Ubuntu (or any Linux-based OS)
- **Programming Language**: Python 3.10+
- **Database**: PostgreSQL
- **Cache Storage**: Valkey
- **Containerization**: Podman
- **Virtual Environment**: Python venv

#### **Required Packages**
- Flask (for backend)
- psycopg2 (for PostgreSQL connectivity)
- redis (for Valkey connection)

### **3. Network Requirements**
- **Ports to be Opened**:
  - 5432 (PostgreSQL)
  - 6379 (Valkey)
  - 5000 (Flask backend)
- **Firewall Rules**: Ensure no blocking on the required ports

---

## **PREREQUISITES**

### **Hardware Requirements**
- Minimum **4GB RAM** (8GB recommended)
- At least **10GB of free disk space**

### **Software Requirements**
- **Operating System**: Ubuntu (or any Linux-based OS)
- **Dependencies**:
  - Git
  - Docker & Podman
  - Python (Ensure Flask is installed)
  - PostgreSQL
  - Valkey

### **Network Requirements**
- **Active internet connection** for pulling the repository and installing dependencies

---

## **STEPS**

### **STEP 1: Clone the Repository**

Command executed:
```sh 
git clone https://github.com/Antar365/Flask_postgres_valkey.git
cd Flask_postgres_valkey
```
Output:
```sh
adarsh@adarsh:~$ git clone https://github.com/Antar365/Flask_postgres_valkey.git
cd Flask_postgres_valkey
Cloning into 'Flask_postgres_valkey'...
remote: Enumerating objects: 2019, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 2019 (delta 2), reused 0 (delta 0), pack-reused 2013 (from 1)
Receiving objects: 100% (2019/2019), 42.22 MiB | 10.53 MiB/s, done.
Resolving deltas: 100% (118/118), done.

```

Verify it is deployed:
```sh 
Run: ls
```

---

### **STEP 2: Set Up the Environment**

Command executed:
```sh 
sudo apt install python3.12-venv
```

Output: 
```sh
adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install python3.12-venv
[sudo] password for adarsh: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-pip-whl python3-setuptools-whl
The following NEW packages will be installed:
  python3-pip-whl python3-setuptools-whl python3.12-venv
0 upgraded, 3 newly installed, 0 to remove and 52 not upgraded.
Need to get 2,424 kB of archives.
After this operation, 2,771 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-pip-whl all 24.0+dfsg-1ubuntu1.1 [1,703 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-setuptools-whl all 68.1.2-2ubuntu1.1 [716 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3.12-venv amd64 3.12.3-1ubuntu0.4 [5,676 B]
Fetched 2,424 kB in 3s (714 kB/s)           
Selecting previously unselected package python3-pip-whl.
(Reading database ... 236912 files and directories currently installed.)
Preparing to unpack .../python3-pip-whl_24.0+dfsg-1ubuntu1.1_all.deb ...
Unpacking python3-pip-whl (24.0+dfsg-1ubuntu1.1) ...
Selecting previously unselected package python3-setuptools-whl.
Preparing to unpack .../python3-setuptools-whl_68.1.2-2ubuntu1.1_all.deb ...
Unpacking python3-setuptools-whl (68.1.2-2ubuntu1.1) ...
Selecting previously unselected package python3.12-venv.
Preparing to unpack .../python3.12-venv_3.12.3-1ubuntu0.4_amd64.deb ...
Unpacking python3.12-venv (3.12.3-1ubuntu0.4) ...
Setting up python3-setuptools-whl (68.1.2-2ubuntu1.1) ...
Setting up python3-pip-whl (24.0+dfsg-1ubuntu1.1) ...
Setting up python3.12-venv (3.12.3-1ubuntu0.4) ...
```
Create Virtual Environment by this command:
```sh
python3 -m venv venv
source venv/bin/activate
```
Output:
```sh
adarsh@adarsh:~/Flask_postgres_valkey$ python3 -m venv venv
adarsh@adarsh:~/Flask_postgres_valkey$ source venv/bin/activate

```
Update System and Install Dependencies:
```sh 
sudo apt update
sudo apt install libpq-dev
```

Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt update
sudo apt install libpq-dev
Ign:1 https://pkg.jenkins.io/debian-stable binary/ InRelease
Hit:2 https://pkg.jenkins.io/debian-stable binary/ Release                                                                                                                        
Get:4 https://dl.google.com/linux/chrome/deb stable InRelease [1,825 B]                                                                                                           
Hit:5 http://in.archive.ubuntu.com/ubuntu noble InRelease                                                                                                           
Get:6 https://dl.google.com/linux/chrome/deb stable/main amd64 Packages [1,217 B]                                                   
Get:7 http://in.archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]                            
Get:8 http://security.ubuntu.com/ubuntu noble-security InRelease [126 kB]      
Hit:9 https://ppa.launchpadcontent.net/flexiondotorg/quickemu/ubuntu noble InRelease     
Get:10 http://in.archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]            
Get:11 http://security.ubuntu.com/ubuntu noble-security/main amd64 Packages [617 kB]
Get:12 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Packages [865 kB]
Get:13 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Components [151 kB]
Get:14 http://in.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Components [212 B]       
Get:15 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Packages [1,014 kB]
Get:16 http://security.ubuntu.com/ubuntu noble-security/main amd64 Components [8,956 B]    
Get:17 http://security.ubuntu.com/ubuntu noble-security/restricted amd64 Components [212 B]
Get:18 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Packages [803 kB]
Get:19 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Components [363 kB]          
Get:20 http://in.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Components [940 B]       
Get:21 http://in.archive.ubuntu.com/ubuntu noble-backports/main amd64 Components [208 B]
Get:22 http://in.archive.ubuntu.com/ubuntu noble-backports/restricted amd64 Components [216 B]
Get:23 http://in.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Components [17.7 kB]
Get:24 http://in.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Components [212 B]                
Get:25 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Components [51.9 kB]                   
Get:26 http://security.ubuntu.com/ubuntu noble-security/multiverse amd64 Components [212 B]
Fetched 4,276 kB in 6s (707 kB/s)                                                                                                                                                                          
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
56 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libpq5
Suggested packages:
  postgresql-doc-16
The following NEW packages will be installed:
  libpq-dev libpq5
0 upgraded, 2 newly installed, 0 to remove and 56 not upgraded.
Need to get 292 kB of archives.
After this operation, 1,031 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpq5 amd64 16.6-0ubuntu0.24.04.1 [141 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpq-dev amd64 16.6-0ubuntu0.24.04.1 [151 kB]
Fetched 292 kB in 3s (84.4 kB/s)   
Selecting previously unselected package libpq5:amd64.
(Reading database ... 236928 files and directories currently installed.)
Preparing to unpack .../libpq5_16.6-0ubuntu0.24.04.1_amd64.deb ...
Unpacking libpq5:amd64 (16.6-0ubuntu0.24.04.1) ...
Selecting previously unselected package libpq-dev.
Preparing to unpack .../libpq-dev_16.6-0ubuntu0.24.04.1_amd64.deb ...
Unpacking libpq-dev (16.6-0ubuntu0.24.04.1) ...
Setting up libpq5:amd64 (16.6-0ubuntu0.24.04.1) ...
Setting up libpq-dev (16.6-0ubuntu0.24.04.1) ...
Processing triggers for libc-bin (2.39-0ubuntu8.3) ...
Processing triggers for man-db (2.12.0-4build2) ...
```

Command Executed

```sh
sudo apt install python3.12-dev
```
Output

```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install python3.12-dev
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3.12-dev is already the newest version (3.12.3-1ubuntu0.4).
python3.12-dev set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 56 not upgraded.
```

Install Required Python Packages:
```sh
pip install -r requirements.txt
```
Output:

```sh


(venv) adarsh@adarsh:~/Flask_postgres_valkey$ pip install -r requirements.txt
Collecting Flask==3.1.0 (from -r requirements.txt (line 1))
  Using cached flask-3.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting psycopg2==2.9.10 (from -r requirements.txt (line 2))
  Using cached psycopg2-2.9.10.tar.gz (385 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting redis==5.2.1 (from -r requirements.txt (line 3))
  Using cached redis-5.2.1-py3-none-any.whl.metadata (9.1 kB)
Collecting psycopg2-binary==2.9.10 (from -r requirements.txt (line 4))
  Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
Collecting Werkzeug>=3.1 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting Jinja2>=3.1.2 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting blinker>=1.9 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->Flask==3.1.0->-r requirements.txt (line 1))
  Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
Using cached flask-3.1.0-py3-none-any.whl (102 kB)
Using cached redis-5.2.1-py3-none-any.whl (261 kB)
Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached click-8.1.8-py3-none-any.whl (98 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.5-py3-none-any.whl (134 kB)
Using cached werkzeug-3.1.3-py3-none-any.whl (224 kB)
Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23 kB)
Building wheels for collected packages: psycopg2
  Building wheel for psycopg2 (pyproject.toml) ... done
  Created wheel for psycopg2: filename=psycopg2-2.9.10-cp312-cp312-linux_x86_64.whl size=529585 sha256=03fc69a13250eddcf4abcdd4ee00b1aca36871d040d0f8df667f7ca54c4acc21
  Stored in directory: /home/adarsh/.cache/pip/wheels/ac/bb/ce/afa589c50b6004d3a06fc691e71bd09c9bd5f01e5921e5329b
Successfully built psycopg2
Installing collected packages: redis, psycopg2-binary, psycopg2, MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, Flask
Successfully installed Flask-3.1.0 Jinja2-3.1.5 MarkupSafe-3.0.2 Werkzeug-3.1.3 blinker-1.9.0 click-8.1.8 itsdangerous-2.2.0 psycopg2-2.9.10 psycopg2-binary-2.9.10 redis-5.2.1

```
Verify Flask Installation:
```sh
python3 -m flask --version
```
---

### **STEP 3: Start the Containers**

Command executed:
```sh
sudo apt install podman-compose
```

Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install podman-compose
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-dotenv
The following NEW packages will be installed:
  podman-compose python3-dotenv
0 upgraded, 2 newly installed, 0 to remove and 56 not upgraded.
Need to get 60.9 kB of archives.
After this operation, 305 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 python3-dotenv all 1.0.1-1 [22.3 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 podman-compose all 1.0.6-1 [38.6 kB]
Fetched 60.9 kB in 2s (35.6 kB/s)        
Selecting previously unselected package python3-dotenv.
(Reading database ... 237341 files and directories currently installed.)
Preparing to unpack .../python3-dotenv_1.0.1-1_all.deb ...
Unpacking python3-dotenv (1.0.1-1) ...
Selecting previously unselected package podman-compose.
Preparing to unpack .../podman-compose_1.0.6-1_all.deb ...
Unpacking podman-compose (1.0.6-1) ...
Setting up python3-dotenv (1.0.1-1) ...
Setting up podman-compose (1.0.6-1) ...
Processing triggers for man-db (2.12.0-4build2) ...


```
---

### **STEP 4: Run the Containers**

Command executed for PostgreSQL:
```sh
podman run -d --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=employee -p 5432:5432 docker.io/library/postgres
```
Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ podman run -d --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=employee -p 5432:5432 docker.io/library/postgres
Trying to pull docker.io/library/postgres:latest...
Getting image source signatures
Copying blob 4553993e7797 done   | 
Copying blob 0dc773e0cc79 done   | 
Copying blob e1ad38ab49c1 done   | 
Copying blob 20f2363da6db done   | 
Copying blob c29f5b76f736 done   | 
Copying blob 559c5c599163 done   | 
Copying blob 91393204ae54 done   | 
Copying blob c0311d3bf51b done   | 
Copying blob 931e444b6b99 done   | 
Copying blob 0de06291fc41 done   | 
Copying blob 1f9512881cf4 done   | 
Copying blob a608baae1e5c done   | 
Copying blob 91befecb86a3 done   | 
Copying blob 8da49c2b3211 done   | 
Copying config d14b06b9a9 done   | 
Writing manifest to image destination
6d2e74dd33bb6ae90e85307e7340766c9386aba58e097e40bd945bc161fb6441
```

Command executed for Valkey:
```sh 
podman run -d --name valkey_container -p 6379:6379 docker.io/valkey/valkey
```
Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ podman run -d --name valkey_container -p 6379:6379 docker.io/valkey/valkey
Trying to pull docker.io/valkey/valkey:latest...
Getting image source signatures
Copying blob c29f5b76f736 skipped: already exists  
Copying blob 4f4fb700ef54 done   | 
Copying blob e9c0e091ec2b done   | 
Copying blob 76d6b73e18e0 done   | 
Copying blob f644cba9db5c done   | 
Copying blob a0a0665da571 done   | 
Copying blob f2bf47372ada done   | 
Copying config df4420e738 done   | 
Writing manifest to image destination
1c89e30b37a9e8bcfa651d4a7dbb1128fd617c5b68f6627eac4e98f8faedc19b
```

Verify PostgreSQL is running:
```sh
podman exec -it postgres_container bash
psql -U postgres
```
---

### **STEP 5: Run the Application**

Command executed:
```sh
python app.py
```# IMPLEMENTATION JOURNAL - Employee Registration Form

## Submitted By:
**Antariksha Rawat**  

## Submitted To:
**Mr. Vipin Tripathi**  

## Test Case Version:

## Reviewer Name:
**Mr. Vipin Tripathi**

---

## **Goal**
This document explains how to pull the project from GitHub and run it on a local machine, ensuring all required dependencies and configurations are met. The project involves using **Flask** in the backend, **PostgreSQL** as the database, and **Valkey** for key-value storage.

---

## **Table of Contents**
### **1. Hardware Requirements**
- **Processor**: Intel Core i5/i7 (or AMD equivalent)
- **RAM**: Minimum 8GB (16GB recommended for better performance)
- **Storage**: At least 20GB of free space
- **Network**: Stable internet connection

### **2. Software Requirements**
- **Operating System**: Ubuntu (or any Linux-based OS)
- **Programming Language**: Python 3.10+
- **Database**: PostgreSQL
- **Cache Storage**: Valkey
- **Containerization**: Podman
- **Virtual Environment**: Python venv

#### **Required Packages**
- Flask (for backend)
- psycopg2 (for PostgreSQL connectivity)
- redis (for Valkey connection)

### **3. Network Requirements**
- **Ports to be Opened**:
  - 5432 (PostgreSQL)
  - 6379 (Valkey)
  - 5000 (Flask backend)
- **Firewall Rules**: Ensure no blocking on the required ports

---

## **PREREQUISITES**

### **Hardware Requirements**
- Minimum **4GB RAM** (8GB recommended)
- At least **10GB of free disk space**

### **Software Requirements**
- **Operating System**: Ubuntu (or any Linux-based OS)
- **Dependencies**:
  - Git
  - Docker & Podman
  - Python (Ensure Flask is installed)
  - PostgreSQL
  - Valkey

### **Network Requirements**
- **Active internet connection** for pulling the repository and installing dependencies

---

## **STEPS**

### **STEP 1: Clone the Repository**

Command executed:
```sh 
git clone https://github.com/Antar365/Flask_postgres_valkey.git
cd Flask_postgres_valkey
```
Output:
```sh
adarsh@adarsh:~$ git clone https://github.com/Antar365/Flask_postgres_valkey.git
cd Flask_postgres_valkey
Cloning into 'Flask_postgres_valkey'...
remote: Enumerating objects: 2019, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 2019 (delta 2), reused 0 (delta 0), pack-reused 2013 (from 1)
Receiving objects: 100% (2019/2019), 42.22 MiB | 10.53 MiB/s, done.
Resolving deltas: 100% (118/118), done.

```

Verify it is deployed:
```sh 
Run: ls
```

---

### **STEP 2: Set Up the Environment**

Command executed:
```sh 
sudo apt install python3.12-venv
```

Output: 
```sh
adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install python3.12-venv
[sudo] password for adarsh: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-pip-whl python3-setuptools-whl
The following NEW packages will be installed:
  python3-pip-whl python3-setuptools-whl python3.12-venv
0 upgraded, 3 newly installed, 0 to remove and 52 not upgraded.
Need to get 2,424 kB of archives.
After this operation, 2,771 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-pip-whl all 24.0+dfsg-1ubuntu1.1 [1,703 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-setuptools-whl all 68.1.2-2ubuntu1.1 [716 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3.12-venv amd64 3.12.3-1ubuntu0.4 [5,676 B]
Fetched 2,424 kB in 3s (714 kB/s)           
Selecting previously unselected package python3-pip-whl.
(Reading database ... 236912 files and directories currently installed.)
Preparing to unpack .../python3-pip-whl_24.0+dfsg-1ubuntu1.1_all.deb ...
Unpacking python3-pip-whl (24.0+dfsg-1ubuntu1.1) ...
Selecting previously unselected package python3-setuptools-whl.
Preparing to unpack .../python3-setuptools-whl_68.1.2-2ubuntu1.1_all.deb ...
Unpacking python3-setuptools-whl (68.1.2-2ubuntu1.1) ...
Selecting previously unselected package python3.12-venv.
Preparing to unpack .../python3.12-venv_3.12.3-1ubuntu0.4_amd64.deb ...
Unpacking python3.12-venv (3.12.3-1ubuntu0.4) ...
Setting up python3-setuptools-whl (68.1.2-2ubuntu1.1) ...
Setting up python3-pip-whl (24.0+dfsg-1ubuntu1.1) ...
Setting up python3.12-venv (3.12.3-1ubuntu0.4) ...
```
Create Virtual Environment by this command:
```sh
python3 -m venv venv
source venv/bin/activate
```
Output:
```sh
adarsh@adarsh:~/Flask_postgres_valkey$ python3 -m venv venv
adarsh@adarsh:~/Flask_postgres_valkey$ source venv/bin/activate

```
Update System and Install Dependencies:
```sh 
sudo apt update
sudo apt install libpq-dev
```

Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt update
sudo apt install libpq-dev
Ign:1 https://pkg.jenkins.io/debian-stable binary/ InRelease
Hit:2 https://pkg.jenkins.io/debian-stable binary/ Release                                                                                                                        
Get:4 https://dl.google.com/linux/chrome/deb stable InRelease [1,825 B]                                                                                                           
Hit:5 http://in.archive.ubuntu.com/ubuntu noble InRelease                                                                                                           
Get:6 https://dl.google.com/linux/chrome/deb stable/main amd64 Packages [1,217 B]                                                   
Get:7 http://in.archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]                            
Get:8 http://security.ubuntu.com/ubuntu noble-security InRelease [126 kB]      
Hit:9 https://ppa.launchpadcontent.net/flexiondotorg/quickemu/ubuntu noble InRelease     
Get:10 http://in.archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]            
Get:11 http://security.ubuntu.com/ubuntu noble-security/main amd64 Packages [617 kB]
Get:12 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Packages [865 kB]
Get:13 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Components [151 kB]
Get:14 http://in.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Components [212 B]       
Get:15 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Packages [1,014 kB]
Get:16 http://security.ubuntu.com/ubuntu noble-security/main amd64 Components [8,956 B]    
Get:17 http://security.ubuntu.com/ubuntu noble-security/restricted amd64 Components [212 B]
Get:18 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Packages [803 kB]
Get:19 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Components [363 kB]          
Get:20 http://in.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Components [940 B]       
Get:21 http://in.archive.ubuntu.com/ubuntu noble-backports/main amd64 Components [208 B]
Get:22 http://in.archive.ubuntu.com/ubuntu noble-backports/restricted amd64 Components [216 B]
Get:23 http://in.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Components [17.7 kB]
Get:24 http://in.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Components [212 B]                
Get:25 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Components [51.9 kB]                   
Get:26 http://security.ubuntu.com/ubuntu noble-security/multiverse amd64 Components [212 B]
Fetched 4,276 kB in 6s (707 kB/s)                                                                                                                                                                          
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
56 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libpq5
Suggested packages:
  postgresql-doc-16
The following NEW packages will be installed:
  libpq-dev libpq5
0 upgraded, 2 newly installed, 0 to remove and 56 not upgraded.
Need to get 292 kB of archives.
After this operation, 1,031 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpq5 amd64 16.6-0ubuntu0.24.04.1 [141 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpq-dev amd64 16.6-0ubuntu0.24.04.1 [151 kB]
Fetched 292 kB in 3s (84.4 kB/s)   
Selecting previously unselected package libpq5:amd64.
(Reading database ... 236928 files and directories currently installed.)
Preparing to unpack .../libpq5_16.6-0ubuntu0.24.04.1_amd64.deb ...
Unpacking libpq5:amd64 (16.6-0ubuntu0.24.04.1) ...
Selecting previously unselected package libpq-dev.
Preparing to unpack .../libpq-dev_16.6-0ubuntu0.24.04.1_amd64.deb ...
Unpacking libpq-dev (16.6-0ubuntu0.24.04.1) ...
Setting up libpq5:amd64 (16.6-0ubuntu0.24.04.1) ...
Setting up libpq-dev (16.6-0ubuntu0.24.04.1) ...
Processing triggers for libc-bin (2.39-0ubuntu8.3) ...
Processing triggers for man-db (2.12.0-4build2) ...
```

Command Executed

```sh
sudo apt install python3.12-dev
```
Output

```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install python3.12-dev
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3.12-dev is already the newest version (3.12.3-1ubuntu0.4).
python3.12-dev set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 56 not upgraded.
```

Install Required Python Packages:
```sh
pip install -r requirements.txt
```
Output:

```sh


(venv) adarsh@adarsh:~/Flask_postgres_valkey$ pip install -r requirements.txt
Collecting Flask==3.1.0 (from -r requirements.txt (line 1))
  Using cached flask-3.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting psycopg2==2.9.10 (from -r requirements.txt (line 2))
  Using cached psycopg2-2.9.10.tar.gz (385 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting redis==5.2.1 (from -r requirements.txt (line 3))
  Using cached redis-5.2.1-py3-none-any.whl.metadata (9.1 kB)
Collecting psycopg2-binary==2.9.10 (from -r requirements.txt (line 4))
  Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
Collecting Werkzeug>=3.1 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting Jinja2>=3.1.2 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting blinker>=1.9 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->Flask==3.1.0->-r requirements.txt (line 1))
  Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
Using cached flask-3.1.0-py3-none-any.whl (102 kB)
Using cached redis-5.2.1-py3-none-any.whl (261 kB)
Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached click-8.1.8-py3-none-any.whl (98 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.5-py3-none-any.whl (134 kB)
Using cached werkzeug-3.1.3-py3-none-any.whl (224 kB)
Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23 kB)
Building wheels for collected packages: psycopg2
  Building wheel for psycopg2 (pyproject.toml) ... done
  Created wheel for psycopg2: filename=psycopg2-2.9.10-cp312-cp312-linux_x86_64.whl size=529585 sha256=03fc69a13250eddcf4abcdd4ee00b1aca36871d040d0f8df667f7ca54c4acc21
  Stored in directory: /home/adarsh/.cache/pip/wheels/ac/bb/ce/afa589c50b6004d3a06fc691e71bd09c9bd5f01e5921e5329b
Successfully built psycopg2
Installing collected packages: redis, psycopg2-binary, psycopg2, MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, Flask
Successfully installed Flask-3.1.0 Jinja2-3.1.5 MarkupSafe-3.0.2 Werkzeug-3.1.3 blinker-1.9.0 click-8.1.8 itsdangerous-2.2.0 psycopg2-2.9.10 psycopg2-binary-2.9.10 redis-5.2.1

```
Verify Flask Installation:
```sh
python3 -m flask --version
```
---

### **STEP 3: Start the Containers**

Command executed:
```sh
sudo apt install podman-compose
```

Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install podman-compose
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-dotenv
The following NEW packages will be installed:
  podman-compose python3-dotenv
0 upgraded, 2 newly installed, 0 to remove and 56 not upgraded.
Need to get 60.9 kB of archives.
After this operation, 305 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 python3-dotenv all 1.0.1-1 [22.3 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 podman-compose all 1.0.6-1 [38.6 kB]
Fetched 60.9 kB in 2s (35.6 kB/s)        
Selecting previously unselected package python3-dotenv.
(Reading database ... 237341 files and directories currently installed.)
Preparing to unpack .../python3-dotenv_1.0.1-1_all.deb ...
Unpacking python3-dotenv (1.0.1-1) ...
Selecting previously unselected package podman-compose.
Preparing to unpack .../podman-compose_1.0.6-1_all.deb ...
Unpacking podman-compose (1.0.6-1) ...
Setting up python3-dotenv (1.0.1-1) ...
Setting up podman-compose (1.0.6-1) ...
Processing triggers for man-db (2.12.0-4build2) ...


```
---

### **STEP 4: Run the Containers**

Command executed for PostgreSQL:
```sh
podman run -d --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=employee -p 5432:5432 docker.io/library/postgres
```
Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ podman run -d --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=employee -p 5432:5432 docker.io/library/postgres
Trying to pull docker.io/library/postgres:latest...
Getting image source signatures
Copying blob 4553993e7797 done   | 
Copying blob 0dc773e0cc79 done   | 
Copying blob e1ad38ab49c1 done   | 
Copying blob 20f2363da6db done   | 
Copying blob c29f5b76f736 done   | 
Copying blob 559c5c599163 done   | 
Copying blob 91393204ae54 done   | 
Copying blob c0311d3bf51b done   | 
Copying blob 931e444b6b99 done   | 
Copying blob 0de06291fc41 done   | 
Copying blob 1f9512881cf4 done   | 
Copying blob a608baae1e5c done   | 
Copying blob 91befecb86a3 done   | 
Copying blob 8da49c2b3211 done   | 
Copying config d14b06b9a9 done   | 
Writing manifest to image destination
6d2e74dd33bb6ae90e85307e7340766c9386aba58e097e40bd945bc161fb6441
```

Command executed for Valkey:
```sh 
podman run -d --name valkey_container -p 6379:6379 docker.io/valkey/valkey
```
Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ podman run -d --name valkey_container -p 6379:6379 docker.io/valkey/valkey
Trying to pull docker.io/valkey/valkey:latest...
Getting image source signatures
Copying blob c29f5b76f736 skipped: already exists  
Copying blob 4f4fb700ef54 done   | 
Copying blob e9c0e091ec2b done   | 
Copying blob 76d6b73e18e0 done   | 
Copying blob f644cba9db5c done   | 
Copying blob a0a0665da571 done   | 
Copying blob f2bf47372ada done   | 
Copying config df4420e738 done   | 
Writing manifest to image destination
1c89e30b37a9e8bcfa651d4a7dbb1128fd617c5b68f6627eac4e98f8faedc19b
```

Verify PostgreSQL is running:
```sh
podman exec -it postgres_container bash
psql -U postgres
```
---

### **STEP 5: Run the Application**

Command executed:
```sh
python app.py
```# IMPLEMENTATION JOURNAL - Employee Registration Form

## Submitted By:
**Antariksha Rawat**  

## Submitted To:
**Mr. Vipin Tripathi**  

## Test Case Version:

## Reviewer Name:
**Mr. Vipin Tripathi**

---

## **Goal**
This document explains how to pull the project from GitHub and run it on a local machine, ensuring all required dependencies and configurations are met. The project involves using **Flask** in the backend, **PostgreSQL** as the database, and **Valkey** for key-value storage.

---

## **Table of Contents**
### **1. Hardware Requirements**
- **Processor**: Intel Core i5/i7 (or AMD equivalent)
- **RAM**: Minimum 8GB (16GB recommended for better performance)
- **Storage**: At least 20GB of free space
- **Network**: Stable internet connection

### **2. Software Requirements**
- **Operating System**: Ubuntu (or any Linux-based OS)
- **Programming Language**: Python 3.10+
- **Database**: PostgreSQL
- **Cache Storage**: Valkey
- **Containerization**: Podman
- **Virtual Environment**: Python venv

#### **Required Packages**
- Flask (for backend)
- psycopg2 (for PostgreSQL connectivity)
- redis (for Valkey connection)

### **3. Network Requirements**
- **Ports to be Opened**:
  - 5432 (PostgreSQL)
  - 6379 (Valkey)
  - 5000 (Flask backend)
- **Firewall Rules**: Ensure no blocking on the required ports

---

## **PREREQUISITES**

### **Hardware Requirements**
- Minimum **4GB RAM** (8GB recommended)
- At least **10GB of free disk space**

### **Software Requirements**
- **Operating System**: Ubuntu (or any Linux-based OS)
- **Dependencies**:
  - Git
  - Docker & Podman
  - Python (Ensure Flask is installed)
  - PostgreSQL
  - Valkey

### **Network Requirements**
- **Active internet connection** for pulling the repository and installing dependencies

---

## **STEPS**

### **STEP 1: Clone the Repository**

Command executed:
```sh 
git clone https://github.com/Antar365/Flask_postgres_valkey.git
cd Flask_postgres_valkey
```
Output:
```sh
adarsh@adarsh:~$ git clone https://github.com/Antar365/Flask_postgres_valkey.git
cd Flask_postgres_valkey
Cloning into 'Flask_postgres_valkey'...
remote: Enumerating objects: 2019, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 2019 (delta 2), reused 0 (delta 0), pack-reused 2013 (from 1)
Receiving objects: 100% (2019/2019), 42.22 MiB | 10.53 MiB/s, done.
Resolving deltas: 100% (118/118), done.

```

Verify it is deployed:
```sh 
Run: ls
```

---

### **STEP 2: Set Up the Environment**

Command executed:
```sh 
sudo apt install python3.12-venv
```

Output: 
```sh
adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install python3.12-venv
[sudo] password for adarsh: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-pip-whl python3-setuptools-whl
The following NEW packages will be installed:
  python3-pip-whl python3-setuptools-whl python3.12-venv
0 upgraded, 3 newly installed, 0 to remove and 52 not upgraded.
Need to get 2,424 kB of archives.
After this operation, 2,771 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-pip-whl all 24.0+dfsg-1ubuntu1.1 [1,703 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-setuptools-whl all 68.1.2-2ubuntu1.1 [716 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3.12-venv amd64 3.12.3-1ubuntu0.4 [5,676 B]
Fetched 2,424 kB in 3s (714 kB/s)           
Selecting previously unselected package python3-pip-whl.
(Reading database ... 236912 files and directories currently installed.)
Preparing to unpack .../python3-pip-whl_24.0+dfsg-1ubuntu1.1_all.deb ...
Unpacking python3-pip-whl (24.0+dfsg-1ubuntu1.1) ...
Selecting previously unselected package python3-setuptools-whl.
Preparing to unpack .../python3-setuptools-whl_68.1.2-2ubuntu1.1_all.deb ...
Unpacking python3-setuptools-whl (68.1.2-2ubuntu1.1) ...
Selecting previously unselected package python3.12-venv.
Preparing to unpack .../python3.12-venv_3.12.3-1ubuntu0.4_amd64.deb ...
Unpacking python3.12-venv (3.12.3-1ubuntu0.4) ...
Setting up python3-setuptools-whl (68.1.2-2ubuntu1.1) ...
Setting up python3-pip-whl (24.0+dfsg-1ubuntu1.1) ...
Setting up python3.12-venv (3.12.3-1ubuntu0.4) ...
```
Create Virtual Environment by this command:
```sh
python3 -m venv venv
source venv/bin/activate
```
Output:
```sh
adarsh@adarsh:~/Flask_postgres_valkey$ python3 -m venv venv
adarsh@adarsh:~/Flask_postgres_valkey$ source venv/bin/activate

```
Update System and Install Dependencies:
```sh 
sudo apt update
sudo apt install libpq-dev
```

Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt update
sudo apt install libpq-dev
Ign:1 https://pkg.jenkins.io/debian-stable binary/ InRelease
Hit:2 https://pkg.jenkins.io/debian-stable binary/ Release                                                                                                                        
Get:4 https://dl.google.com/linux/chrome/deb stable InRelease [1,825 B]                                                                                                           
Hit:5 http://in.archive.ubuntu.com/ubuntu noble InRelease                                                                                                           
Get:6 https://dl.google.com/linux/chrome/deb stable/main amd64 Packages [1,217 B]                                                   
Get:7 http://in.archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]                            
Get:8 http://security.ubuntu.com/ubuntu noble-security InRelease [126 kB]      
Hit:9 https://ppa.launchpadcontent.net/flexiondotorg/quickemu/ubuntu noble InRelease     
Get:10 http://in.archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]            
Get:11 http://security.ubuntu.com/ubuntu noble-security/main amd64 Packages [617 kB]
Get:12 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Packages [865 kB]
Get:13 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Components [151 kB]
Get:14 http://in.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Components [212 B]       
Get:15 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Packages [1,014 kB]
Get:16 http://security.ubuntu.com/ubuntu noble-security/main amd64 Components [8,956 B]    
Get:17 http://security.ubuntu.com/ubuntu noble-security/restricted amd64 Components [212 B]
Get:18 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Packages [803 kB]
Get:19 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Components [363 kB]          
Get:20 http://in.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Components [940 B]       
Get:21 http://in.archive.ubuntu.com/ubuntu noble-backports/main amd64 Components [208 B]
Get:22 http://in.archive.ubuntu.com/ubuntu noble-backports/restricted amd64 Components [216 B]
Get:23 http://in.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Components [17.7 kB]
Get:24 http://in.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Components [212 B]                
Get:25 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Components [51.9 kB]                   
Get:26 http://security.ubuntu.com/ubuntu noble-security/multiverse amd64 Components [212 B]
Fetched 4,276 kB in 6s (707 kB/s)                                                                                                                                                                          
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
56 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libpq5
Suggested packages:
  postgresql-doc-16
The following NEW packages will be installed:
  libpq-dev libpq5
0 upgraded, 2 newly installed, 0 to remove and 56 not upgraded.
Need to get 292 kB of archives.
After this operation, 1,031 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpq5 amd64 16.6-0ubuntu0.24.04.1 [141 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpq-dev amd64 16.6-0ubuntu0.24.04.1 [151 kB]
Fetched 292 kB in 3s (84.4 kB/s)   
Selecting previously unselected package libpq5:amd64.
(Reading database ... 236928 files and directories currently installed.)
Preparing to unpack .../libpq5_16.6-0ubuntu0.24.04.1_amd64.deb ...
Unpacking libpq5:amd64 (16.6-0ubuntu0.24.04.1) ...
Selecting previously unselected package libpq-dev.
Preparing to unpack .../libpq-dev_16.6-0ubuntu0.24.04.1_amd64.deb ...
Unpacking libpq-dev (16.6-0ubuntu0.24.04.1) ...
Setting up libpq5:amd64 (16.6-0ubuntu0.24.04.1) ...
Setting up libpq-dev (16.6-0ubuntu0.24.04.1) ...
Processing triggers for libc-bin (2.39-0ubuntu8.3) ...
Processing triggers for man-db (2.12.0-4build2) ...
```

Command Executed

```sh
sudo apt install python3.12-dev
```
Output

```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install python3.12-dev
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3.12-dev is already the newest version (3.12.3-1ubuntu0.4).
python3.12-dev set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 56 not upgraded.
```

Install Required Python Packages:
```sh
pip install -r requirements.txt
```
Output:

```sh


(venv) adarsh@adarsh:~/Flask_postgres_valkey$ pip install -r requirements.txt
Collecting Flask==3.1.0 (from -r requirements.txt (line 1))
  Using cached flask-3.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting psycopg2==2.9.10 (from -r requirements.txt (line 2))
  Using cached psycopg2-2.9.10.tar.gz (385 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting redis==5.2.1 (from -r requirements.txt (line 3))
  Using cached redis-5.2.1-py3-none-any.whl.metadata (9.1 kB)
Collecting psycopg2-binary==2.9.10 (from -r requirements.txt (line 4))
  Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
Collecting Werkzeug>=3.1 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting Jinja2>=3.1.2 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting blinker>=1.9 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->Flask==3.1.0->-r requirements.txt (line 1))
  Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
Using cached flask-3.1.0-py3-none-any.whl (102 kB)
Using cached redis-5.2.1-py3-none-any.whl (261 kB)
Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached click-8.1.8-py3-none-any.whl (98 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.5-py3-none-any.whl (134 kB)
Using cached werkzeug-3.1.3-py3-none-any.whl (224 kB)
Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23 kB)
Building wheels for collected packages: psycopg2
  Building wheel for psycopg2 (pyproject.toml) ... done
  Created wheel for psycopg2: filename=psycopg2-2.9.10-cp312-cp312-linux_x86_64.whl size=529585 sha256=03fc69a13250eddcf4abcdd4ee00b1aca36871d040d0f8df667f7ca54c4acc21
  Stored in directory: /home/adarsh/.cache/pip/wheels/ac/bb/ce/afa589c50b6004d3a06fc691e71bd09c9bd5f01e5921e5329b
Successfully built psycopg2
Installing collected packages: redis, psycopg2-binary, psycopg2, MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, Flask
Successfully installed Flask-3.1.0 Jinja2-3.1.5 MarkupSafe-3.0.2 Werkzeug-3.1.3 blinker-1.9.0 click-8.1.8 itsdangerous-2.2.0 psycopg2-2.9.10 psycopg2-binary-2.9.10 redis-5.2.1

```
Verify Flask Installation:
```sh
python3 -m flask --version
```
---

### **STEP 3: Start the Containers**

Command executed:
```sh
sudo apt install podman-compose
```

Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install podman-compose
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-dotenv
The following NEW packages will be installed:
  podman-compose python3-dotenv
0 upgraded, 2 newly installed, 0 to remove and 56 not upgraded.
Need to get 60.9 kB of archives.
After this operation, 305 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 python3-dotenv all 1.0.1-1 [22.3 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 podman-compose all 1.0.6-1 [38.6 kB]
Fetched 60.9 kB in 2s (35.6 kB/s)        
Selecting previously unselected package python3-dotenv.
(Reading database ... 237341 files and directories currently installed.)
Preparing to unpack .../python3-dotenv_1.0.1-1_all.deb ...
Unpacking python3-dotenv (1.0.1-1) ...
Selecting previously unselected package podman-compose.
Preparing to unpack .../podman-compose_1.0.6-1_all.deb ...
Unpacking podman-compose (1.0.6-1) ...
Setting up python3-dotenv (1.0.1-1) ...
Setting up podman-compose (1.0.6-1) ...
Processing triggers for man-db (2.12.0-4build2) ...


```
---

### **STEP 4: Run the Containers**

Command executed for PostgreSQL:
```sh
podman run -d --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=employee -p 5432:5432 docker.io/library/postgres
```
Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ podman run -d --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=employee -p 5432:5432 docker.io/library/postgres
Trying to pull docker.io/library/postgres:latest...
Getting image source signatures
Copying blob 4553993e7797 done   | 
Copying blob 0dc773e0cc79 done   | 
Copying blob e1ad38ab49c1 done   | 
Copying blob 20f2363da6db done   | 
Copying blob c29f5b76f736 done   | 
Copying blob 559c5c599163 done   | 
Copying blob 91393204ae54 done   | 
Copying blob c0311d3bf51b done   | 
Copying blob 931e444b6b99 done   | 
Copying blob 0de06291fc41 done   | 
Copying blob 1f9512881cf4 done   | 
Copying blob a608baae1e5c done   | 
Copying blob 91befecb86a3 done   | 
Copying blob 8da49c2b3211 done   | 
Copying config d14b06b9a9 done   | 
Writing manifest to image destination
6d2e74dd33bb6ae90e85307e7340766c9386aba58e097e40bd945bc161fb6441
```

Command executed for Valkey:
```sh 
podman run -d --name valkey_container -p 6379:6379 docker.io/valkey/valkey
```
Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ podman run -d --name valkey_container -p 6379:6379 docker.io/valkey/valkey
Trying to pull docker.io/valkey/valkey:latest...
Getting image source signatures
Copying blob c29f5b76f736 skipped: already exists  
Copying blob 4f4fb700ef54 done   | 
Copying blob e9c0e091ec2b done   | 
Copying blob 76d6b73e18e0 done   | 
Copying blob f644cba9db5c done   | 
Copying blob a0a0665da571 done   | 
Copying blob f2bf47372ada done   | 
Copying config df4420e738 done   | 
Writing manifest to image destination
1c89e30b37a9e8bcfa651d4a7dbb1128fd617c5b68f6627eac4e98f8faedc19b
```

Verify PostgreSQL is running:
```sh
podman exec -it postgres_container bash
psql -U postgres
```
---

### **STEP 5: Run the Application**

Command executed:
```sh
python app.py
```# IMPLEMENTATION JOURNAL - Employee Registration Form

## Submitted By:
**Antariksha Rawat**  

## Submitted To:
**Mr. Vipin Tripathi**  

## Test Case Version:

## Reviewer Name:
**Mr. Vipin Tripathi**

---

## **Goal**
This document explains how to pull the project from GitHub and run it on a local machine, ensuring all required dependencies and configurations are met. The project involves using **Flask** in the backend, **PostgreSQL** as the database, and **Valkey** for key-value storage.

---

## **Table of Contents**
### **1. Hardware Requirements**
- **Processor**: Intel Core i5/i7 (or AMD equivalent)
- **RAM**: Minimum 8GB (16GB recommended for better performance)
- **Storage**: At least 20GB of free space
- **Network**: Stable internet connection

### **2. Software Requirements**
- **Operating System**: Ubuntu (or any Linux-based OS)
- **Programming Language**: Python 3.10+
- **Database**: PostgreSQL
- **Cache Storage**: Valkey
- **Containerization**: Podman
- **Virtual Environment**: Python venv

#### **Required Packages**
- Flask (for backend)
- psycopg2 (for PostgreSQL connectivity)
- redis (for Valkey connection)

### **3. Network Requirements**
- **Ports to be Opened**:
  - 5432 (PostgreSQL)
  - 6379 (Valkey)
  - 5000 (Flask backend)
- **Firewall Rules**: Ensure no blocking on the required ports

---

## **PREREQUISITES**

### **Hardware Requirements**
- Minimum **4GB RAM** (8GB recommended)
- At least **10GB of free disk space**

### **Software Requirements**
- **Operating System**: Ubuntu (or any Linux-based OS)
- **Dependencies**:
  - Git
  - Docker & Podman
  - Python (Ensure Flask is installed)
  - PostgreSQL
  - Valkey

### **Network Requirements**
- **Active internet connection** for pulling the repository and installing dependencies

---

## **STEPS**

### **STEP 1: Clone the Repository**

Command executed:
```sh 
git clone https://github.com/Antar365/Flask_postgres_valkey.git
cd Flask_postgres_valkey
```
Output:
```sh
adarsh@adarsh:~$ git clone https://github.com/Antar365/Flask_postgres_valkey.git
cd Flask_postgres_valkey
Cloning into 'Flask_postgres_valkey'...
remote: Enumerating objects: 2019, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 2019 (delta 2), reused 0 (delta 0), pack-reused 2013 (from 1)
Receiving objects: 100% (2019/2019), 42.22 MiB | 10.53 MiB/s, done.
Resolving deltas: 100% (118/118), done.

```

Verify it is deployed:
```sh 
Run: ls
```

---

### **STEP 2: Set Up the Environment**

Command executed:
```sh 
sudo apt install python3.12-venv
```

Output: 
```sh
adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install python3.12-venv
[sudo] password for adarsh: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-pip-whl python3-setuptools-whl
The following NEW packages will be installed:
  python3-pip-whl python3-setuptools-whl python3.12-venv
0 upgraded, 3 newly installed, 0 to remove and 52 not upgraded.
Need to get 2,424 kB of archives.
After this operation, 2,771 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-pip-whl all 24.0+dfsg-1ubuntu1.1 [1,703 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-setuptools-whl all 68.1.2-2ubuntu1.1 [716 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3.12-venv amd64 3.12.3-1ubuntu0.4 [5,676 B]
Fetched 2,424 kB in 3s (714 kB/s)           
Selecting previously unselected package python3-pip-whl.
(Reading database ... 236912 files and directories currently installed.)
Preparing to unpack .../python3-pip-whl_24.0+dfsg-1ubuntu1.1_all.deb ...
Unpacking python3-pip-whl (24.0+dfsg-1ubuntu1.1) ...
Selecting previously unselected package python3-setuptools-whl.
Preparing to unpack .../python3-setuptools-whl_68.1.2-2ubuntu1.1_all.deb ...
Unpacking python3-setuptools-whl (68.1.2-2ubuntu1.1) ...
Selecting previously unselected package python3.12-venv.
Preparing to unpack .../python3.12-venv_3.12.3-1ubuntu0.4_amd64.deb ...
Unpacking python3.12-venv (3.12.3-1ubuntu0.4) ...
Setting up python3-setuptools-whl (68.1.2-2ubuntu1.1) ...
Setting up python3-pip-whl (24.0+dfsg-1ubuntu1.1) ...
Setting up python3.12-venv (3.12.3-1ubuntu0.4) ...
```
Create Virtual Environment by this command:
```sh
python3 -m venv venv
source venv/bin/activate
```
Output:
```sh
adarsh@adarsh:~/Flask_postgres_valkey$ python3 -m venv venv
adarsh@adarsh:~/Flask_postgres_valkey$ source venv/bin/activate

```
Update System and Install Dependencies:
```sh 
sudo apt update
sudo apt install libpq-dev
```

Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt update
sudo apt install libpq-dev
Ign:1 https://pkg.jenkins.io/debian-stable binary/ InRelease
Hit:2 https://pkg.jenkins.io/debian-stable binary/ Release                                                                                                                        
Get:4 https://dl.google.com/linux/chrome/deb stable InRelease [1,825 B]                                                                                                           
Hit:5 http://in.archive.ubuntu.com/ubuntu noble InRelease                                                                                                           
Get:6 https://dl.google.com/linux/chrome/deb stable/main amd64 Packages [1,217 B]                                                   
Get:7 http://in.archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]                            
Get:8 http://security.ubuntu.com/ubuntu noble-security InRelease [126 kB]      
Hit:9 https://ppa.launchpadcontent.net/flexiondotorg/quickemu/ubuntu noble InRelease     
Get:10 http://in.archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]            
Get:11 http://security.ubuntu.com/ubuntu noble-security/main amd64 Packages [617 kB]
Get:12 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Packages [865 kB]
Get:13 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Components [151 kB]
Get:14 http://in.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Components [212 B]       
Get:15 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Packages [1,014 kB]
Get:16 http://security.ubuntu.com/ubuntu noble-security/main amd64 Components [8,956 B]    
Get:17 http://security.ubuntu.com/ubuntu noble-security/restricted amd64 Components [212 B]
Get:18 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Packages [803 kB]
Get:19 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Components [363 kB]          
Get:20 http://in.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Components [940 B]       
Get:21 http://in.archive.ubuntu.com/ubuntu noble-backports/main amd64 Components [208 B]
Get:22 http://in.archive.ubuntu.com/ubuntu noble-backports/restricted amd64 Components [216 B]
Get:23 http://in.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Components [17.7 kB]
Get:24 http://in.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Components [212 B]                
Get:25 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Components [51.9 kB]                   
Get:26 http://security.ubuntu.com/ubuntu noble-security/multiverse amd64 Components [212 B]
Fetched 4,276 kB in 6s (707 kB/s)                                                                                                                                                                          
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
56 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libpq5
Suggested packages:
  postgresql-doc-16
The following NEW packages will be installed:
  libpq-dev libpq5
0 upgraded, 2 newly installed, 0 to remove and 56 not upgraded.
Need to get 292 kB of archives.
After this operation, 1,031 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpq5 amd64 16.6-0ubuntu0.24.04.1 [141 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpq-dev amd64 16.6-0ubuntu0.24.04.1 [151 kB]
Fetched 292 kB in 3s (84.4 kB/s)   
Selecting previously unselected package libpq5:amd64.
(Reading database ... 236928 files and directories currently installed.)
Preparing to unpack .../libpq5_16.6-0ubuntu0.24.04.1_amd64.deb ...
Unpacking libpq5:amd64 (16.6-0ubuntu0.24.04.1) ...
Selecting previously unselected package libpq-dev.
Preparing to unpack .../libpq-dev_16.6-0ubuntu0.24.04.1_amd64.deb ...
Unpacking libpq-dev (16.6-0ubuntu0.24.04.1) ...
Setting up libpq5:amd64 (16.6-0ubuntu0.24.04.1) ...
Setting up libpq-dev (16.6-0ubuntu0.24.04.1) ...
Processing triggers for libc-bin (2.39-0ubuntu8.3) ...
Processing triggers for man-db (2.12.0-4build2) ...
```

Command Executed

```sh
sudo apt install python3.12-dev
```
Output

```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install python3.12-dev
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3.12-dev is already the newest version (3.12.3-1ubuntu0.4).
python3.12-dev set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 56 not upgraded.
```

Install Required Python Packages:
```sh
pip install -r requirements.txt
```
Output:

```sh


(venv) adarsh@adarsh:~/Flask_postgres_valkey$ pip install -r requirements.txt
Collecting Flask==3.1.0 (from -r requirements.txt (line 1))
  Using cached flask-3.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting psycopg2==2.9.10 (from -r requirements.txt (line 2))
  Using cached psycopg2-2.9.10.tar.gz (385 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting redis==5.2.1 (from -r requirements.txt (line 3))
  Using cached redis-5.2.1-py3-none-any.whl.metadata (9.1 kB)
Collecting psycopg2-binary==2.9.10 (from -r requirements.txt (line 4))
  Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
Collecting Werkzeug>=3.1 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting Jinja2>=3.1.2 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting blinker>=1.9 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->Flask==3.1.0->-r requirements.txt (line 1))
  Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
Using cached flask-3.1.0-py3-none-any.whl (102 kB)
Using cached redis-5.2.1-py3-none-any.whl (261 kB)
Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached click-8.1.8-py3-none-any.whl (98 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.5-py3-none-any.whl (134 kB)
Using cached werkzeug-3.1.3-py3-none-any.whl (224 kB)
Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23 kB)
Building wheels for collected packages: psycopg2
  Building wheel for psycopg2 (pyproject.toml) ... done
  Created wheel for psycopg2: filename=psycopg2-2.9.10-cp312-cp312-linux_x86_64.whl size=529585 sha256=03fc69a13250eddcf4abcdd4ee00b1aca36871d040d0f8df667f7ca54c4acc21
  Stored in directory: /home/adarsh/.cache/pip/wheels/ac/bb/ce/afa589c50b6004d3a06fc691e71bd09c9bd5f01e5921e5329b
Successfully built psycopg2
Installing collected packages: redis, psycopg2-binary, psycopg2, MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, Flask
Successfully installed Flask-3.1.0 Jinja2-3.1.5 MarkupSafe-3.0.2 Werkzeug-3.1.3 blinker-1.9.0 click-8.1.8 itsdangerous-2.2.0 psycopg2-2.9.10 psycopg2-binary-2.9.10 redis-5.2.1

```
Verify Flask Installation:
```sh
python3 -m flask --version
```
---

### **STEP 3: Start the Containers**

Command executed:
```sh
sudo apt install podman-compose
```

Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install podman-compose
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-dotenv
The following NEW packages will be installed:
  podman-compose python3-dotenv
0 upgraded, 2 newly installed, 0 to remove and 56 not upgraded.
Need to get 60.9 kB of archives.
After this operation, 305 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 python3-dotenv all 1.0.1-1 [22.3 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 podman-compose all 1.0.6-1 [38.6 kB]
Fetched 60.9 kB in 2s (35.6 kB/s)        
Selecting previously unselected package python3-dotenv.
(Reading database ... 237341 files and directories currently installed.)
Preparing to unpack .../python3-dotenv_1.0.1-1_all.deb ...
Unpacking python3-dotenv (1.0.1-1) ...
Selecting previously unselected package podman-compose.
Preparing to unpack .../podman-compose_1.0.6-1_all.deb ...
Unpacking podman-compose (1.0.6-1) ...
Setting up python3-dotenv (1.0.1-1) ...
Setting up podman-compose (1.0.6-1) ...
Processing triggers for man-db (2.12.0-4build2) ...


```
---

### **STEP 4: Run the Containers**

Command executed for PostgreSQL:
```sh
podman run -d --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=employee -p 5432:5432 docker.io/library/postgres
```
Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ podman run -d --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=employee -p 5432:5432 docker.io/library/postgres
Trying to pull docker.io/library/postgres:latest...
Getting image source signatures
Copying blob 4553993e7797 done   | 
Copying blob 0dc773e0cc79 done   | 
Copying blob e1ad38ab49c1 done   | 
Copying blob 20f2363da6db done   | 
Copying blob c29f5b76f736 done   | 
Copying blob 559c5c599163 done   | 
Copying blob 91393204ae54 done   | 
Copying blob c0311d3bf51b done   | 
Copying blob 931e444b6b99 done   | 
Copying blob 0de06291fc41 done   | 
Copying blob 1f9512881cf4 done   | 
Copying blob a608baae1e5c done   | 
Copying blob 91befecb86a3 done   | 
Copying blob 8da49c2b3211 done   | 
Copying config d14b06b9a9 done   | 
Writing manifest to image destination
6d2e74dd33bb6ae90e85307e7340766c9386aba58e097e40bd945bc161fb6441
```

Command executed for Valkey:
```sh 
podman run -d --name valkey_container -p 6379:6379 docker.io/valkey/valkey
```
Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ podman run -d --name valkey_container -p 6379:6379 docker.io/valkey/valkey
Trying to pull docker.io/valkey/valkey:latest...
Getting image source signatures
Copying blob c29f5b76f736 skipped: already exists  
Copying blob 4f4fb700ef54 done   | 
Copying blob e9c0e091ec2b done   | 
Copying blob 76d6b73e18e0 done   | 
Copying blob f644cba9db5c done   | 
Copying blob a0a0665da571 done   | 
Copying blob f2bf47372ada done   | 
Copying config df4420e738 done   | 
Writing manifest to image destination
1c89e30b37a9e8bcfa651d4a7dbb1128fd617c5b68f6627eac4e98f8faedc19b
```

Verify PostgreSQL is running:
```sh
podman exec -it postgres_container bash
psql -U postgres
```
---

### **STEP 5: Run the Application**

Command executed:
```sh
python app.py
```# IMPLEMENTATION JOURNAL - Employee Registration Form

## Submitted By:
**Antariksha Rawat**  

## Submitted To:
**Mr. Vipin Tripathi**  

## Test Case Version:

## Reviewer Name:
**Mr. Vipin Tripathi**

---

## **Goal**
This document explains how to pull the project from GitHub and run it on a local machine, ensuring all required dependencies and configurations are met. The project involves using **Flask** in the backend, **PostgreSQL** as the database, and **Valkey** for key-value storage.

---

## **Table of Contents**
### **1. Hardware Requirements**
- **Processor**: Intel Core i5/i7 (or AMD equivalent)
- **RAM**: Minimum 8GB (16GB recommended for better performance)
- **Storage**: At least 20GB of free space
- **Network**: Stable internet connection

### **2. Software Requirements**
- **Operating System**: Ubuntu (or any Linux-based OS)
- **Programming Language**: Python 3.10+
- **Database**: PostgreSQL
- **Cache Storage**: Valkey
- **Containerization**: Podman
- **Virtual Environment**: Python venv

#### **Required Packages**
- Flask (for backend)
- psycopg2 (for PostgreSQL connectivity)
- redis (for Valkey connection)

### **3. Network Requirements**
- **Ports to be Opened**:
  - 5432 (PostgreSQL)
  - 6379 (Valkey)
  - 5000 (Flask backend)
- **Firewall Rules**: Ensure no blocking on the required ports

---

## **PREREQUISITES**

### **Hardware Requirements**
- Minimum **4GB RAM** (8GB recommended)
- At least **10GB of free disk space**

### **Software Requirements**
- **Operating System**: Ubuntu (or any Linux-based OS)
- **Dependencies**:
  - Git
  - Docker & Podman
  - Python (Ensure Flask is installed)
  - PostgreSQL
  - Valkey

### **Network Requirements**
- **Active internet connection** for pulling the repository and installing dependencies

---

## **STEPS**

### **STEP 1: Clone the Repository**

Command executed:
```sh 
git clone https://github.com/Antar365/Flask_postgres_valkey.git
cd Flask_postgres_valkey
```
Output:
```sh
adarsh@adarsh:~$ git clone https://github.com/Antar365/Flask_postgres_valkey.git
cd Flask_postgres_valkey
Cloning into 'Flask_postgres_valkey'...
remote: Enumerating objects: 2019, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 2019 (delta 2), reused 0 (delta 0), pack-reused 2013 (from 1)
Receiving objects: 100% (2019/2019), 42.22 MiB | 10.53 MiB/s, done.
Resolving deltas: 100% (118/118), done.

```

Verify it is deployed:
```sh 
Run: ls
```

---

### **STEP 2: Set Up the Environment**

Command executed:
```sh 
sudo apt install python3.12-venv
```

Output: 
```sh
adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install python3.12-venv
[sudo] password for adarsh: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-pip-whl python3-setuptools-whl
The following NEW packages will be installed:
  python3-pip-whl python3-setuptools-whl python3.12-venv
0 upgraded, 3 newly installed, 0 to remove and 52 not upgraded.
Need to get 2,424 kB of archives.
After this operation, 2,771 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-pip-whl all 24.0+dfsg-1ubuntu1.1 [1,703 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-setuptools-whl all 68.1.2-2ubuntu1.1 [716 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3.12-venv amd64 3.12.3-1ubuntu0.4 [5,676 B]
Fetched 2,424 kB in 3s (714 kB/s)           
Selecting previously unselected package python3-pip-whl.
(Reading database ... 236912 files and directories currently installed.)
Preparing to unpack .../python3-pip-whl_24.0+dfsg-1ubuntu1.1_all.deb ...
Unpacking python3-pip-whl (24.0+dfsg-1ubuntu1.1) ...
Selecting previously unselected package python3-setuptools-whl.
Preparing to unpack .../python3-setuptools-whl_68.1.2-2ubuntu1.1_all.deb ...
Unpacking python3-setuptools-whl (68.1.2-2ubuntu1.1) ...
Selecting previously unselected package python3.12-venv.
Preparing to unpack .../python3.12-venv_3.12.3-1ubuntu0.4_amd64.deb ...
Unpacking python3.12-venv (3.12.3-1ubuntu0.4) ...
Setting up python3-setuptools-whl (68.1.2-2ubuntu1.1) ...
Setting up python3-pip-whl (24.0+dfsg-1ubuntu1.1) ...
Setting up python3.12-venv (3.12.3-1ubuntu0.4) ...
```
Create Virtual Environment by this command:
```sh
python3 -m venv venv
source venv/bin/activate
```
Output:
```sh
adarsh@adarsh:~/Flask_postgres_valkey$ python3 -m venv venv
adarsh@adarsh:~/Flask_postgres_valkey$ source venv/bin/activate

```
Update System and Install Dependencies:
```sh 
sudo apt update
sudo apt install libpq-dev
```

Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt update
sudo apt install libpq-dev
Ign:1 https://pkg.jenkins.io/debian-stable binary/ InRelease
Hit:2 https://pkg.jenkins.io/debian-stable binary/ Release                                                                                                                        
Get:4 https://dl.google.com/linux/chrome/deb stable InRelease [1,825 B]                                                                                                           
Hit:5 http://in.archive.ubuntu.com/ubuntu noble InRelease                                                                                                           
Get:6 https://dl.google.com/linux/chrome/deb stable/main amd64 Packages [1,217 B]                                                   
Get:7 http://in.archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]                            
Get:8 http://security.ubuntu.com/ubuntu noble-security InRelease [126 kB]      
Hit:9 https://ppa.launchpadcontent.net/flexiondotorg/quickemu/ubuntu noble InRelease     
Get:10 http://in.archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]            
Get:11 http://security.ubuntu.com/ubuntu noble-security/main amd64 Packages [617 kB]
Get:12 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Packages [865 kB]
Get:13 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Components [151 kB]
Get:14 http://in.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Components [212 B]       
Get:15 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Packages [1,014 kB]
Get:16 http://security.ubuntu.com/ubuntu noble-security/main amd64 Components [8,956 B]    
Get:17 http://security.ubuntu.com/ubuntu noble-security/restricted amd64 Components [212 B]
Get:18 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Packages [803 kB]
Get:19 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Components [363 kB]          
Get:20 http://in.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Components [940 B]       
Get:21 http://in.archive.ubuntu.com/ubuntu noble-backports/main amd64 Components [208 B]
Get:22 http://in.archive.ubuntu.com/ubuntu noble-backports/restricted amd64 Components [216 B]
Get:23 http://in.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Components [17.7 kB]
Get:24 http://in.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Components [212 B]                
Get:25 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Components [51.9 kB]                   
Get:26 http://security.ubuntu.com/ubuntu noble-security/multiverse amd64 Components [212 B]
Fetched 4,276 kB in 6s (707 kB/s)                                                                                                                                                                          
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
56 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libpq5
Suggested packages:
  postgresql-doc-16
The following NEW packages will be installed:
  libpq-dev libpq5
0 upgraded, 2 newly installed, 0 to remove and 56 not upgraded.
Need to get 292 kB of archives.
After this operation, 1,031 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpq5 amd64 16.6-0ubuntu0.24.04.1 [141 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpq-dev amd64 16.6-0ubuntu0.24.04.1 [151 kB]
Fetched 292 kB in 3s (84.4 kB/s)   
Selecting previously unselected package libpq5:amd64.
(Reading database ... 236928 files and directories currently installed.)
Preparing to unpack .../libpq5_16.6-0ubuntu0.24.04.1_amd64.deb ...
Unpacking libpq5:amd64 (16.6-0ubuntu0.24.04.1) ...
Selecting previously unselected package libpq-dev.
Preparing to unpack .../libpq-dev_16.6-0ubuntu0.24.04.1_amd64.deb ...
Unpacking libpq-dev (16.6-0ubuntu0.24.04.1) ...
Setting up libpq5:amd64 (16.6-0ubuntu0.24.04.1) ...
Setting up libpq-dev (16.6-0ubuntu0.24.04.1) ...
Processing triggers for libc-bin (2.39-0ubuntu8.3) ...
Processing triggers for man-db (2.12.0-4build2) ...
```

Command Executed

```sh
sudo apt install python3.12-dev
```
Output

```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install python3.12-dev
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3.12-dev is already the newest version (3.12.3-1ubuntu0.4).
python3.12-dev set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 56 not upgraded.
```

Install Required Python Packages:
```sh
pip install -r requirements.txt
```
Output:

```sh


(venv) adarsh@adarsh:~/Flask_postgres_valkey$ pip install -r requirements.txt
Collecting Flask==3.1.0 (from -r requirements.txt (line 1))
  Using cached flask-3.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting psycopg2==2.9.10 (from -r requirements.txt (line 2))
  Using cached psycopg2-2.9.10.tar.gz (385 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting redis==5.2.1 (from -r requirements.txt (line 3))
  Using cached redis-5.2.1-py3-none-any.whl.metadata (9.1 kB)
Collecting psycopg2-binary==2.9.10 (from -r requirements.txt (line 4))
  Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
Collecting Werkzeug>=3.1 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting Jinja2>=3.1.2 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting blinker>=1.9 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->Flask==3.1.0->-r requirements.txt (line 1))
  Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
Using cached flask-3.1.0-py3-none-any.whl (102 kB)
Using cached redis-5.2.1-py3-none-any.whl (261 kB)
Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached click-8.1.8-py3-none-any.whl (98 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.5-py3-none-any.whl (134 kB)
Using cached werkzeug-3.1.3-py3-none-any.whl (224 kB)
Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23 kB)
Building wheels for collected packages: psycopg2
  Building wheel for psycopg2 (pyproject.toml) ... done
  Created wheel for psycopg2: filename=psycopg2-2.9.10-cp312-cp312-linux_x86_64.whl size=529585 sha256=03fc69a13250eddcf4abcdd4ee00b1aca36871d040d0f8df667f7ca54c4acc21
  Stored in directory: /home/adarsh/.cache/pip/wheels/ac/bb/ce/afa589c50b6004d3a06fc691e71bd09c9bd5f01e5921e5329b
Successfully built psycopg2
Installing collected packages: redis, psycopg2-binary, psycopg2, MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, Flask
Successfully installed Flask-3.1.0 Jinja2-3.1.5 MarkupSafe-3.0.2 Werkzeug-3.1.3 blinker-1.9.0 click-8.1.8 itsdangerous-2.2.0 psycopg2-2.9.10 psycopg2-binary-2.9.10 redis-5.2.1

```
Verify Flask Installation:
```sh
python3 -m flask --version
```
---

### **STEP 3: Start the Containers**

Command executed:
```sh
sudo apt install podman-compose
```

Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install podman-compose
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-dotenv
The following NEW packages will be installed:
  podman-compose python3-dotenv
0 upgraded, 2 newly installed, 0 to remove and 56 not upgraded.
Need to get 60.9 kB of archives.
After this operation, 305 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 python3-dotenv all 1.0.1-1 [22.3 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 podman-compose all 1.0.6-1 [38.6 kB]
Fetched 60.9 kB in 2s (35.6 kB/s)        
Selecting previously unselected package python3-dotenv.
(Reading database ... 237341 files and directories currently installed.)
Preparing to unpack .../python3-dotenv_1.0.1-1_all.deb ...
Unpacking python3-dotenv (1.0.1-1) ...
Selecting previously unselected package podman-compose.
Preparing to unpack .../podman-compose_1.0.6-1_all.deb ...
Unpacking podman-compose (1.0.6-1) ...
Setting up python3-dotenv (1.0.1-1) ...
Setting up podman-compose (1.0.6-1) ...
Processing triggers for man-db (2.12.0-4build2) ...


```
---

### **STEP 4: Run the Containers**

Command executed for PostgreSQL:
```sh
podman run -d --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=employee -p 5432:5432 docker.io/library/postgres
```
Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ podman run -d --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=employee -p 5432:5432 docker.io/library/postgres
Trying to pull docker.io/library/postgres:latest...
Getting image source signatures
Copying blob 4553993e7797 done   | 
Copying blob 0dc773e0cc79 done   | 
Copying blob e1ad38ab49c1 done   | 
Copying blob 20f2363da6db done   | 
Copying blob c29f5b76f736 done   | 
Copying blob 559c5c599163 done   | 
Copying blob 91393204ae54 done   | 
Copying blob c0311d3bf51b done   | 
Copying blob 931e444b6b99 done   | 
Copying blob 0de06291fc41 done   | 
Copying blob 1f9512881cf4 done   | 
Copying blob a608baae1e5c done   | 
Copying blob 91befecb86a3 done   | 
Copying blob 8da49c2b3211 done   | 
Copying config d14b06b9a9 done   | 
Writing manifest to image destination
6d2e74dd33bb6ae90e85307e7340766c9386aba58e097e40bd945bc161fb6441
```

Command executed for Valkey:
```sh 
podman run -d --name valkey_container -p 6379:6379 docker.io/valkey/valkey
```
Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ podman run -d --name valkey_container -p 6379:6379 docker.io/valkey/valkey
Trying to pull docker.io/valkey/valkey:latest...
Getting image source signatures
Copying blob c29f5b76f736 skipped: already exists  
Copying blob 4f4fb700ef54 done   | 
Copying blob e9c0e091ec2b done   | 
Copying blob 76d6b73e18e0 done   | 
Copying blob f644cba9db5c done   | 
Copying blob a0a0665da571 done   | 
Copying blob f2bf47372ada done   | 
Copying config df4420e738 done   | 
Writing manifest to image destination
1c89e30b37a9e8bcfa651d4a7dbb1128fd617c5b68f6627eac4e98f8faedc19b
```

Verify PostgreSQL is running:
```sh
podman exec -it postgres_container bash
psql -U postgres
```
---

### **STEP 5: Run the Application**

Command executed:
```sh
python app.py
```# IMPLEMENTATION JOURNAL - Employee Registration Form

## Submitted By:
**Antariksha Rawat**  

## Submitted To:
**Mr. Vipin Tripathi**  

## Test Case Version:

## Reviewer Name:
**Mr. Vipin Tripathi**

---

## **Goal**
This document explains how to pull the project from GitHub and run it on a local machine, ensuring all required dependencies and configurations are met. The project involves using **Flask** in the backend, **PostgreSQL** as the database, and **Valkey** for key-value storage.

---

## **Table of Contents**
### **1. Hardware Requirements**
- **Processor**: Intel Core i5/i7 (or AMD equivalent)
- **RAM**: Minimum 8GB (16GB recommended for better performance)
- **Storage**: At least 20GB of free space
- **Network**: Stable internet connection

### **2. Software Requirements**
- **Operating System**: Ubuntu (or any Linux-based OS)
- **Programming Language**: Python 3.10+
- **Database**: PostgreSQL
- **Cache Storage**: Valkey
- **Containerization**: Podman
- **Virtual Environment**: Python venv

#### **Required Packages**
- Flask (for backend)
- psycopg2 (for PostgreSQL connectivity)
- redis (for Valkey connection)

### **3. Network Requirements**
- **Ports to be Opened**:
  - 5432 (PostgreSQL)
  - 6379 (Valkey)
  - 5000 (Flask backend)
- **Firewall Rules**: Ensure no blocking on the required ports

---

## **PREREQUISITES**

### **Hardware Requirements**
- Minimum **4GB RAM** (8GB recommended)
- At least **10GB of free disk space**

### **Software Requirements**
- **Operating System**: Ubuntu (or any Linux-based OS)
- **Dependencies**:
  - Git
  - Docker & Podman
  - Python (Ensure Flask is installed)
  - PostgreSQL
  - Valkey

### **Network Requirements**
- **Active internet connection** for pulling the repository and installing dependencies

---

## **STEPS**

### **STEP 1: Clone the Repository**

Command executed:
```sh 
git clone https://github.com/Antar365/Flask_postgres_valkey.git
cd Flask_postgres_valkey
```
Output:
```sh
adarsh@adarsh:~$ git clone https://github.com/Antar365/Flask_postgres_valkey.git
cd Flask_postgres_valkey
Cloning into 'Flask_postgres_valkey'...
remote: Enumerating objects: 2019, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 2019 (delta 2), reused 0 (delta 0), pack-reused 2013 (from 1)
Receiving objects: 100% (2019/2019), 42.22 MiB | 10.53 MiB/s, done.
Resolving deltas: 100% (118/118), done.

```

Verify it is deployed:
```sh 
Run: ls
```

---

### **STEP 2: Set Up the Environment**

Command executed:
```sh 
sudo apt install python3.12-venv
```

Output: 
```sh
adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install python3.12-venv
[sudo] password for adarsh: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-pip-whl python3-setuptools-whl
The following NEW packages will be installed:
  python3-pip-whl python3-setuptools-whl python3.12-venv
0 upgraded, 3 newly installed, 0 to remove and 52 not upgraded.
Need to get 2,424 kB of archives.
After this operation, 2,771 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-pip-whl all 24.0+dfsg-1ubuntu1.1 [1,703 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-setuptools-whl all 68.1.2-2ubuntu1.1 [716 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3.12-venv amd64 3.12.3-1ubuntu0.4 [5,676 B]
Fetched 2,424 kB in 3s (714 kB/s)           
Selecting previously unselected package python3-pip-whl.
(Reading database ... 236912 files and directories currently installed.)
Preparing to unpack .../python3-pip-whl_24.0+dfsg-1ubuntu1.1_all.deb ...
Unpacking python3-pip-whl (24.0+dfsg-1ubuntu1.1) ...
Selecting previously unselected package python3-setuptools-whl.
Preparing to unpack .../python3-setuptools-whl_68.1.2-2ubuntu1.1_all.deb ...
Unpacking python3-setuptools-whl (68.1.2-2ubuntu1.1) ...
Selecting previously unselected package python3.12-venv.
Preparing to unpack .../python3.12-venv_3.12.3-1ubuntu0.4_amd64.deb ...
Unpacking python3.12-venv (3.12.3-1ubuntu0.4) ...
Setting up python3-setuptools-whl (68.1.2-2ubuntu1.1) ...
Setting up python3-pip-whl (24.0+dfsg-1ubuntu1.1) ...
Setting up python3.12-venv (3.12.3-1ubuntu0.4) ...
```
Create Virtual Environment by this command:
```sh
python3 -m venv venv
source venv/bin/activate
```
Output:
```sh
adarsh@adarsh:~/Flask_postgres_valkey$ python3 -m venv venv
adarsh@adarsh:~/Flask_postgres_valkey$ source venv/bin/activate

```
Update System and Install Dependencies:
```sh 
sudo apt update
sudo apt install libpq-dev
```

Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt update
sudo apt install libpq-dev
Ign:1 https://pkg.jenkins.io/debian-stable binary/ InRelease
Hit:2 https://pkg.jenkins.io/debian-stable binary/ Release                                                                                                                        
Get:4 https://dl.google.com/linux/chrome/deb stable InRelease [1,825 B]                                                                                                           
Hit:5 http://in.archive.ubuntu.com/ubuntu noble InRelease                                                                                                           
Get:6 https://dl.google.com/linux/chrome/deb stable/main amd64 Packages [1,217 B]                                                   
Get:7 http://in.archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]                            
Get:8 http://security.ubuntu.com/ubuntu noble-security InRelease [126 kB]      
Hit:9 https://ppa.launchpadcontent.net/flexiondotorg/quickemu/ubuntu noble InRelease     
Get:10 http://in.archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]            
Get:11 http://security.ubuntu.com/ubuntu noble-security/main amd64 Packages [617 kB]
Get:12 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Packages [865 kB]
Get:13 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Components [151 kB]
Get:14 http://in.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Components [212 B]       
Get:15 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Packages [1,014 kB]
Get:16 http://security.ubuntu.com/ubuntu noble-security/main amd64 Components [8,956 B]    
Get:17 http://security.ubuntu.com/ubuntu noble-security/restricted amd64 Components [212 B]
Get:18 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Packages [803 kB]
Get:19 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Components [363 kB]          
Get:20 http://in.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Components [940 B]       
Get:21 http://in.archive.ubuntu.com/ubuntu noble-backports/main amd64 Components [208 B]
Get:22 http://in.archive.ubuntu.com/ubuntu noble-backports/restricted amd64 Components [216 B]
Get:23 http://in.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Components [17.7 kB]
Get:24 http://in.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Components [212 B]                
Get:25 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Components [51.9 kB]                   
Get:26 http://security.ubuntu.com/ubuntu noble-security/multiverse amd64 Components [212 B]
Fetched 4,276 kB in 6s (707 kB/s)                                                                                                                                                                          
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
56 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libpq5
Suggested packages:
  postgresql-doc-16
The following NEW packages will be installed:
  libpq-dev libpq5
0 upgraded, 2 newly installed, 0 to remove and 56 not upgraded.
Need to get 292 kB of archives.
After this operation, 1,031 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpq5 amd64 16.6-0ubuntu0.24.04.1 [141 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpq-dev amd64 16.6-0ubuntu0.24.04.1 [151 kB]
Fetched 292 kB in 3s (84.4 kB/s)   
Selecting previously unselected package libpq5:amd64.
(Reading database ... 236928 files and directories currently installed.)
Preparing to unpack .../libpq5_16.6-0ubuntu0.24.04.1_amd64.deb ...
Unpacking libpq5:amd64 (16.6-0ubuntu0.24.04.1) ...
Selecting previously unselected package libpq-dev.
Preparing to unpack .../libpq-dev_16.6-0ubuntu0.24.04.1_amd64.deb ...
Unpacking libpq-dev (16.6-0ubuntu0.24.04.1) ...
Setting up libpq5:amd64 (16.6-0ubuntu0.24.04.1) ...
Setting up libpq-dev (16.6-0ubuntu0.24.04.1) ...
Processing triggers for libc-bin (2.39-0ubuntu8.3) ...
Processing triggers for man-db (2.12.0-4build2) ...
```

Command Executed

```sh
sudo apt install python3.12-dev
```
Output

```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install python3.12-dev
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3.12-dev is already the newest version (3.12.3-1ubuntu0.4).
python3.12-dev set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 56 not upgraded.
```

Install Required Python Packages:
```sh
pip install -r requirements.txt
```
Output:

```sh


(venv) adarsh@adarsh:~/Flask_postgres_valkey$ pip install -r requirements.txt
Collecting Flask==3.1.0 (from -r requirements.txt (line 1))
  Using cached flask-3.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting psycopg2==2.9.10 (from -r requirements.txt (line 2))
  Using cached psycopg2-2.9.10.tar.gz (385 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting redis==5.2.1 (from -r requirements.txt (line 3))
  Using cached redis-5.2.1-py3-none-any.whl.metadata (9.1 kB)
Collecting psycopg2-binary==2.9.10 (from -r requirements.txt (line 4))
  Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
Collecting Werkzeug>=3.1 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting Jinja2>=3.1.2 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting blinker>=1.9 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->Flask==3.1.0->-r requirements.txt (line 1))
  Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
Using cached flask-3.1.0-py3-none-any.whl (102 kB)
Using cached redis-5.2.1-py3-none-any.whl (261 kB)
Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached click-8.1.8-py3-none-any.whl (98 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.5-py3-none-any.whl (134 kB)
Using cached werkzeug-3.1.3-py3-none-any.whl (224 kB)
Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23 kB)
Building wheels for collected packages: psycopg2
  Building wheel for psycopg2 (pyproject.toml) ... done
  Created wheel for psycopg2: filename=psycopg2-2.9.10-cp312-cp312-linux_x86_64.whl size=529585 sha256=03fc69a13250eddcf4abcdd4ee00b1aca36871d040d0f8df667f7ca54c4acc21
  Stored in directory: /home/adarsh/.cache/pip/wheels/ac/bb/ce/afa589c50b6004d3a06fc691e71bd09c9bd5f01e5921e5329b
Successfully built psycopg2
Installing collected packages: redis, psycopg2-binary, psycopg2, MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, Flask
Successfully installed Flask-3.1.0 Jinja2-3.1.5 MarkupSafe-3.0.2 Werkzeug-3.1.3 blinker-1.9.0 click-8.1.8 itsdangerous-2.2.0 psycopg2-2.9.10 psycopg2-binary-2.9.10 redis-5.2.1

```
Verify Flask Installation:
```sh
python3 -m flask --version
```
---

### **STEP 3: Start the Containers**

Command executed:
```sh
sudo apt install podman-compose
```

Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install podman-compose
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-dotenv
The following NEW packages will be installed:
  podman-compose python3-dotenv
0 upgraded, 2 newly installed, 0 to remove and 56 not upgraded.
Need to get 60.9 kB of archives.
After this operation, 305 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 python3-dotenv all 1.0.1-1 [22.3 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 podman-compose all 1.0.6-1 [38.6 kB]
Fetched 60.9 kB in 2s (35.6 kB/s)        
Selecting previously unselected package python3-dotenv.
(Reading database ... 237341 files and directories currently installed.)
Preparing to unpack .../python3-dotenv_1.0.1-1_all.deb ...
Unpacking python3-dotenv (1.0.1-1) ...
Selecting previously unselected package podman-compose.
Preparing to unpack .../podman-compose_1.0.6-1_all.deb ...
Unpacking podman-compose (1.0.6-1) ...
Setting up python3-dotenv (1.0.1-1) ...
Setting up podman-compose (1.0.6-1) ...
Processing triggers for man-db (2.12.0-4build2) ...


```
---

### **STEP 4: Run the Containers**

Command executed for PostgreSQL:
```sh
podman run -d --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=employee -p 5432:5432 docker.io/library/postgres
```
Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ podman run -d --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=employee -p 5432:5432 docker.io/library/postgres
Trying to pull docker.io/library/postgres:latest...
Getting image source signatures
Copying blob 4553993e7797 done   | 
Copying blob 0dc773e0cc79 done   | 
Copying blob e1ad38ab49c1 done   | 
Copying blob 20f2363da6db done   | 
Copying blob c29f5b76f736 done   | 
Copying blob 559c5c599163 done   | 
Copying blob 91393204ae54 done   | 
Copying blob c0311d3bf51b done   | 
Copying blob 931e444b6b99 done   | 
Copying blob 0de06291fc41 done   | 
Copying blob 1f9512881cf4 done   | 
Copying blob a608baae1e5c done   | 
Copying blob 91befecb86a3 done   | 
Copying blob 8da49c2b3211 done   | 
Copying config d14b06b9a9 done   | 
Writing manifest to image destination
6d2e74dd33bb6ae90e85307e7340766c9386aba58e097e40bd945bc161fb6441
```

Command executed for Valkey:
```sh 
podman run -d --name valkey_container -p 6379:6379 docker.io/valkey/valkey
```
Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ podman run -d --name valkey_container -p 6379:6379 docker.io/valkey/valkey
Trying to pull docker.io/valkey/valkey:latest...
Getting image source signatures
Copying blob c29f5b76f736 skipped: already exists  
Copying blob 4f4fb700ef54 done   | 
Copying blob e9c0e091ec2b done   | 
Copying blob 76d6b73e18e0 done   | 
Copying blob f644cba9db5c done   | 
Copying blob a0a0665da571 done   | 
Copying blob f2bf47372ada done   | 
Copying config df4420e738 done   | 
Writing manifest to image destination
1c89e30b37a9e8bcfa651d4a7dbb1128fd617c5b68f6627eac4e98f8faedc19b
```

Verify PostgreSQL is running:
```sh
podman exec -it postgres_container bash
psql -U postgres
```
---

### **STEP 5: Run the Application**

Command executed:
```sh
python app.py
```# IMPLEMENTATION JOURNAL - Employee Registration Form

## Submitted By:
**Antariksha Rawat**  

## Submitted To:
**Mr. Vipin Tripathi**  

## Test Case Version:

## Reviewer Name:
**Mr. Vipin Tripathi**

---

## **Goal**
This document explains how to pull the project from GitHub and run it on a local machine, ensuring all required dependencies and configurations are met. The project involves using **Flask** in the backend, **PostgreSQL** as the database, and **Valkey** for key-value storage.

---

## **Table of Contents**
### **1. Hardware Requirements**
- **Processor**: Intel Core i5/i7 (or AMD equivalent)
- **RAM**: Minimum 8GB (16GB recommended for better performance)
- **Storage**: At least 20GB of free space
- **Network**: Stable internet connection

### **2. Software Requirements**
- **Operating System**: Ubuntu (or any Linux-based OS)
- **Programming Language**: Python 3.10+
- **Database**: PostgreSQL
- **Cache Storage**: Valkey
- **Containerization**: Podman
- **Virtual Environment**: Python venv

#### **Required Packages**
- Flask (for backend)
- psycopg2 (for PostgreSQL connectivity)
- redis (for Valkey connection)

### **3. Network Requirements**
- **Ports to be Opened**:
  - 5432 (PostgreSQL)
  - 6379 (Valkey)
  - 5000 (Flask backend)
- **Firewall Rules**: Ensure no blocking on the required ports

---

## **PREREQUISITES**

### **Hardware Requirements**
- Minimum **4GB RAM** (8GB recommended)
- At least **10GB of free disk space**

### **Software Requirements**
- **Operating System**: Ubuntu (or any Linux-based OS)
- **Dependencies**:
  - Git
  - Docker & Podman
  - Python (Ensure Flask is installed)
  - PostgreSQL
  - Valkey

### **Network Requirements**
- **Active internet connection** for pulling the repository and installing dependencies

---

## **STEPS**

### **STEP 1: Clone the Repository**

Command executed:
```sh 
git clone https://github.com/Antar365/Flask_postgres_valkey.git
cd Flask_postgres_valkey
```
Output:
```sh
adarsh@adarsh:~$ git clone https://github.com/Antar365/Flask_postgres_valkey.git
cd Flask_postgres_valkey
Cloning into 'Flask_postgres_valkey'...
remote: Enumerating objects: 2019, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 2019 (delta 2), reused 0 (delta 0), pack-reused 2013 (from 1)
Receiving objects: 100% (2019/2019), 42.22 MiB | 10.53 MiB/s, done.
Resolving deltas: 100% (118/118), done.

```

Verify it is deployed:
```sh 
Run: ls
```

---

### **STEP 2: Set Up the Environment**

Command executed:
```sh 
sudo apt install python3.12-venv
```

Output: 
```sh
adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install python3.12-venv
[sudo] password for adarsh: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-pip-whl python3-setuptools-whl
The following NEW packages will be installed:
  python3-pip-whl python3-setuptools-whl python3.12-venv
0 upgraded, 3 newly installed, 0 to remove and 52 not upgraded.
Need to get 2,424 kB of archives.
After this operation, 2,771 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-pip-whl all 24.0+dfsg-1ubuntu1.1 [1,703 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-setuptools-whl all 68.1.2-2ubuntu1.1 [716 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3.12-venv amd64 3.12.3-1ubuntu0.4 [5,676 B]
Fetched 2,424 kB in 3s (714 kB/s)           
Selecting previously unselected package python3-pip-whl.
(Reading database ... 236912 files and directories currently installed.)
Preparing to unpack .../python3-pip-whl_24.0+dfsg-1ubuntu1.1_all.deb ...
Unpacking python3-pip-whl (24.0+dfsg-1ubuntu1.1) ...
Selecting previously unselected package python3-setuptools-whl.
Preparing to unpack .../python3-setuptools-whl_68.1.2-2ubuntu1.1_all.deb ...
Unpacking python3-setuptools-whl (68.1.2-2ubuntu1.1) ...
Selecting previously unselected package python3.12-venv.
Preparing to unpack .../python3.12-venv_3.12.3-1ubuntu0.4_amd64.deb ...
Unpacking python3.12-venv (3.12.3-1ubuntu0.4) ...
Setting up python3-setuptools-whl (68.1.2-2ubuntu1.1) ...
Setting up python3-pip-whl (24.0+dfsg-1ubuntu1.1) ...
Setting up python3.12-venv (3.12.3-1ubuntu0.4) ...
```
Create Virtual Environment by this command:
```sh
python3 -m venv venv
source venv/bin/activate
```
Output:
```sh
adarsh@adarsh:~/Flask_postgres_valkey$ python3 -m venv venv
adarsh@adarsh:~/Flask_postgres_valkey$ source venv/bin/activate

```
Update System and Install Dependencies:
```sh 
sudo apt update
sudo apt install libpq-dev
```

Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt update
sudo apt install libpq-dev
Ign:1 https://pkg.jenkins.io/debian-stable binary/ InRelease
Hit:2 https://pkg.jenkins.io/debian-stable binary/ Release                                                                                                                        
Get:4 https://dl.google.com/linux/chrome/deb stable InRelease [1,825 B]                                                                                                           
Hit:5 http://in.archive.ubuntu.com/ubuntu noble InRelease                                                                                                           
Get:6 https://dl.google.com/linux/chrome/deb stable/main amd64 Packages [1,217 B]                                                   
Get:7 http://in.archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]                            
Get:8 http://security.ubuntu.com/ubuntu noble-security InRelease [126 kB]      
Hit:9 https://ppa.launchpadcontent.net/flexiondotorg/quickemu/ubuntu noble InRelease     
Get:10 http://in.archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]            
Get:11 http://security.ubuntu.com/ubuntu noble-security/main amd64 Packages [617 kB]
Get:12 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Packages [865 kB]
Get:13 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Components [151 kB]
Get:14 http://in.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Components [212 B]       
Get:15 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Packages [1,014 kB]
Get:16 http://security.ubuntu.com/ubuntu noble-security/main amd64 Components [8,956 B]    
Get:17 http://security.ubuntu.com/ubuntu noble-security/restricted amd64 Components [212 B]
Get:18 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Packages [803 kB]
Get:19 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Components [363 kB]          
Get:20 http://in.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Components [940 B]       
Get:21 http://in.archive.ubuntu.com/ubuntu noble-backports/main amd64 Components [208 B]
Get:22 http://in.archive.ubuntu.com/ubuntu noble-backports/restricted amd64 Components [216 B]
Get:23 http://in.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Components [17.7 kB]
Get:24 http://in.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Components [212 B]                
Get:25 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Components [51.9 kB]                   
Get:26 http://security.ubuntu.com/ubuntu noble-security/multiverse amd64 Components [212 B]
Fetched 4,276 kB in 6s (707 kB/s)                                                                                                                                                                          
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
56 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libpq5
Suggested packages:
  postgresql-doc-16
The following NEW packages will be installed:
  libpq-dev libpq5
0 upgraded, 2 newly installed, 0 to remove and 56 not upgraded.
Need to get 292 kB of archives.
After this operation, 1,031 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpq5 amd64 16.6-0ubuntu0.24.04.1 [141 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpq-dev amd64 16.6-0ubuntu0.24.04.1 [151 kB]
Fetched 292 kB in 3s (84.4 kB/s)   
Selecting previously unselected package libpq5:amd64.
(Reading database ... 236928 files and directories currently installed.)
Preparing to unpack .../libpq5_16.6-0ubuntu0.24.04.1_amd64.deb ...
Unpacking libpq5:amd64 (16.6-0ubuntu0.24.04.1) ...
Selecting previously unselected package libpq-dev.
Preparing to unpack .../libpq-dev_16.6-0ubuntu0.24.04.1_amd64.deb ...
Unpacking libpq-dev (16.6-0ubuntu0.24.04.1) ...
Setting up libpq5:amd64 (16.6-0ubuntu0.24.04.1) ...
Setting up libpq-dev (16.6-0ubuntu0.24.04.1) ...
Processing triggers for libc-bin (2.39-0ubuntu8.3) ...
Processing triggers for man-db (2.12.0-4build2) ...
```

Command Executed

```sh
sudo apt install python3.12-dev
```
Output

```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install python3.12-dev
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3.12-dev is already the newest version (3.12.3-1ubuntu0.4).
python3.12-dev set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 56 not upgraded.
```

Install Required Python Packages:
```sh
pip install -r requirements.txt
```
Output:

```sh


(venv) adarsh@adarsh:~/Flask_postgres_valkey$ pip install -r requirements.txt
Collecting Flask==3.1.0 (from -r requirements.txt (line 1))
  Using cached flask-3.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting psycopg2==2.9.10 (from -r requirements.txt (line 2))
  Using cached psycopg2-2.9.10.tar.gz (385 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting redis==5.2.1 (from -r requirements.txt (line 3))
  Using cached redis-5.2.1-py3-none-any.whl.metadata (9.1 kB)
Collecting psycopg2-binary==2.9.10 (from -r requirements.txt (line 4))
  Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
Collecting Werkzeug>=3.1 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting Jinja2>=3.1.2 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting blinker>=1.9 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->Flask==3.1.0->-r requirements.txt (line 1))
  Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
Using cached flask-3.1.0-py3-none-any.whl (102 kB)
Using cached redis-5.2.1-py3-none-any.whl (261 kB)
Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached click-8.1.8-py3-none-any.whl (98 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.5-py3-none-any.whl (134 kB)
Using cached werkzeug-3.1.3-py3-none-any.whl (224 kB)
Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23 kB)
Building wheels for collected packages: psycopg2
  Building wheel for psycopg2 (pyproject.toml) ... done
  Created wheel for psycopg2: filename=psycopg2-2.9.10-cp312-cp312-linux_x86_64.whl size=529585 sha256=03fc69a13250eddcf4abcdd4ee00b1aca36871d040d0f8df667f7ca54c4acc21
  Stored in directory: /home/adarsh/.cache/pip/wheels/ac/bb/ce/afa589c50b6004d3a06fc691e71bd09c9bd5f01e5921e5329b
Successfully built psycopg2
Installing collected packages: redis, psycopg2-binary, psycopg2, MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, Flask
Successfully installed Flask-3.1.0 Jinja2-3.1.5 MarkupSafe-3.0.2 Werkzeug-3.1.3 blinker-1.9.0 click-8.1.8 itsdangerous-2.2.0 psycopg2-2.9.10 psycopg2-binary-2.9.10 redis-5.2.1

```
Verify Flask Installation:
```sh
python3 -m flask --version
```
---

### **STEP 3: Start the Containers**

Command executed:
```sh
sudo apt install podman-compose
```

Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install podman-compose
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-dotenv
The following NEW packages will be installed:
  podman-compose python3-dotenv
0 upgraded, 2 newly installed, 0 to remove and 56 not upgraded.
Need to get 60.9 kB of archives.
After this operation, 305 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 python3-dotenv all 1.0.1-1 [22.3 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 podman-compose all 1.0.6-1 [38.6 kB]
Fetched 60.9 kB in 2s (35.6 kB/s)        
Selecting previously unselected package python3-dotenv.
(Reading database ... 237341 files and directories currently installed.)
Preparing to unpack .../python3-dotenv_1.0.1-1_all.deb ...
Unpacking python3-dotenv (1.0.1-1) ...
Selecting previously unselected package podman-compose.
Preparing to unpack .../podman-compose_1.0.6-1_all.deb ...
Unpacking podman-compose (1.0.6-1) ...
Setting up python3-dotenv (1.0.1-1) ...
Setting up podman-compose (1.0.6-1) ...
Processing triggers for man-db (2.12.0-4build2) ...


```
---

### **STEP 4: Run the Containers**

Command executed for PostgreSQL:
```sh
podman run -d --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=employee -p 5432:5432 docker.io/library/postgres
```
Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ podman run -d --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=employee -p 5432:5432 docker.io/library/postgres
Trying to pull docker.io/library/postgres:latest...
Getting image source signatures
Copying blob 4553993e7797 done   | 
Copying blob 0dc773e0cc79 done   | 
Copying blob e1ad38ab49c1 done   | 
Copying blob 20f2363da6db done   | 
Copying blob c29f5b76f736 done   | 
Copying blob 559c5c599163 done   | 
Copying blob 91393204ae54 done   | 
Copying blob c0311d3bf51b done   | 
Copying blob 931e444b6b99 done   | 
Copying blob 0de06291fc41 done   | 
Copying blob 1f9512881cf4 done   | 
Copying blob a608baae1e5c done   | 
Copying blob 91befecb86a3 done   | 
Copying blob 8da49c2b3211 done   | 
Copying config d14b06b9a9 done   | 
Writing manifest to image destination
6d2e74dd33bb6ae90e85307e7340766c9386aba58e097e40bd945bc161fb6441
```

Command executed for Valkey:
```sh 
podman run -d --name valkey_container -p 6379:6379 docker.io/valkey/valkey
```
Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ podman run -d --name valkey_container -p 6379:6379 docker.io/valkey/valkey
Trying to pull docker.io/valkey/valkey:latest...
Getting image source signatures
Copying blob c29f5b76f736 skipped: already exists  
Copying blob 4f4fb700ef54 done   | 
Copying blob e9c0e091ec2b done   | 
Copying blob 76d6b73e18e0 done   | 
Copying blob f644cba9db5c done   | 
Copying blob a0a0665da571 done   | 
Copying blob f2bf47372ada done   | 
Copying config df4420e738 done   | 
Writing manifest to image destination
1c89e30b37a9e8bcfa651d4a7dbb1128fd617c5b68f6627eac4e98f8faedc19b
```

Verify PostgreSQL is running:
```sh
podman exec -it postgres_container bash
psql -U postgres
```
---

### **STEP 5: Run the Application**

Command executed:
```sh
python app.py
```# IMPLEMENTATION JOURNAL - Employee Registration Form

## Submitted By:
**Antariksha Rawat**  

## Submitted To:
**Mr. Vipin Tripathi**  

## Test Case Version:

## Reviewer Name:
**Mr. Vipin Tripathi**

---

## **Goal**
This document explains how to pull the project from GitHub and run it on a local machine, ensuring all required dependencies and configurations are met. The project involves using **Flask** in the backend, **PostgreSQL** as the database, and **Valkey** for key-value storage.

---

## **Table of Contents**
### **1. Hardware Requirements**
- **Processor**: Intel Core i5/i7 (or AMD equivalent)
- **RAM**: Minimum 8GB (16GB recommended for better performance)
- **Storage**: At least 20GB of free space
- **Network**: Stable internet connection

### **2. Software Requirements**
- **Operating System**: Ubuntu (or any Linux-based OS)
- **Programming Language**: Python 3.10+
- **Database**: PostgreSQL
- **Cache Storage**: Valkey
- **Containerization**: Podman
- **Virtual Environment**: Python venv

#### **Required Packages**
- Flask (for backend)
- psycopg2 (for PostgreSQL connectivity)
- redis (for Valkey connection)

### **3. Network Requirements**
- **Ports to be Opened**:
  - 5432 (PostgreSQL)
  - 6379 (Valkey)
  - 5000 (Flask backend)
- **Firewall Rules**: Ensure no blocking on the required ports

---

## **PREREQUISITES**

### **Hardware Requirements**
- Minimum **4GB RAM** (8GB recommended)
- At least **10GB of free disk space**

### **Software Requirements**
- **Operating System**: Ubuntu (or any Linux-based OS)
- **Dependencies**:
  - Git
  - Docker & Podman
  - Python (Ensure Flask is installed)
  - PostgreSQL
  - Valkey

### **Network Requirements**
- **Active internet connection** for pulling the repository and installing dependencies

---

## **STEPS**

### **STEP 1: Clone the Repository**

Command executed:
```sh 
git clone https://github.com/Antar365/Flask_postgres_valkey.git
cd Flask_postgres_valkey
```
Output:
```sh
adarsh@adarsh:~$ git clone https://github.com/Antar365/Flask_postgres_valkey.git
cd Flask_postgres_valkey
Cloning into 'Flask_postgres_valkey'...
remote: Enumerating objects: 2019, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 2019 (delta 2), reused 0 (delta 0), pack-reused 2013 (from 1)
Receiving objects: 100% (2019/2019), 42.22 MiB | 10.53 MiB/s, done.
Resolving deltas: 100% (118/118), done.

```

Verify it is deployed:
```sh 
Run: ls
```

---

### **STEP 2: Set Up the Environment**

Command executed:
```sh 
sudo apt install python3.12-venv
```

Output: 
```sh
adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install python3.12-venv
[sudo] password for adarsh: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-pip-whl python3-setuptools-whl
The following NEW packages will be installed:
  python3-pip-whl python3-setuptools-whl python3.12-venv
0 upgraded, 3 newly installed, 0 to remove and 52 not upgraded.
Need to get 2,424 kB of archives.
After this operation, 2,771 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-pip-whl all 24.0+dfsg-1ubuntu1.1 [1,703 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-setuptools-whl all 68.1.2-2ubuntu1.1 [716 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3.12-venv amd64 3.12.3-1ubuntu0.4 [5,676 B]
Fetched 2,424 kB in 3s (714 kB/s)           
Selecting previously unselected package python3-pip-whl.
(Reading database ... 236912 files and directories currently installed.)
Preparing to unpack .../python3-pip-whl_24.0+dfsg-1ubuntu1.1_all.deb ...
Unpacking python3-pip-whl (24.0+dfsg-1ubuntu1.1) ...
Selecting previously unselected package python3-setuptools-whl.
Preparing to unpack .../python3-setuptools-whl_68.1.2-2ubuntu1.1_all.deb ...
Unpacking python3-setuptools-whl (68.1.2-2ubuntu1.1) ...
Selecting previously unselected package python3.12-venv.
Preparing to unpack .../python3.12-venv_3.12.3-1ubuntu0.4_amd64.deb ...
Unpacking python3.12-venv (3.12.3-1ubuntu0.4) ...
Setting up python3-setuptools-whl (68.1.2-2ubuntu1.1) ...
Setting up python3-pip-whl (24.0+dfsg-1ubuntu1.1) ...
Setting up python3.12-venv (3.12.3-1ubuntu0.4) ...
```
Create Virtual Environment by this command:
```sh
python3 -m venv venv
source venv/bin/activate
```
Output:
```sh
adarsh@adarsh:~/Flask_postgres_valkey$ python3 -m venv venv
adarsh@adarsh:~/Flask_postgres_valkey$ source venv/bin/activate

```
Update System and Install Dependencies:
```sh 
sudo apt update
sudo apt install libpq-dev
```

Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt update
sudo apt install libpq-dev
Ign:1 https://pkg.jenkins.io/debian-stable binary/ InRelease
Hit:2 https://pkg.jenkins.io/debian-stable binary/ Release                                                                                                                        
Get:4 https://dl.google.com/linux/chrome/deb stable InRelease [1,825 B]                                                                                                           
Hit:5 http://in.archive.ubuntu.com/ubuntu noble InRelease                                                                                                           
Get:6 https://dl.google.com/linux/chrome/deb stable/main amd64 Packages [1,217 B]                                                   
Get:7 http://in.archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]                            
Get:8 http://security.ubuntu.com/ubuntu noble-security InRelease [126 kB]      
Hit:9 https://ppa.launchpadcontent.net/flexiondotorg/quickemu/ubuntu noble InRelease     
Get:10 http://in.archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]            
Get:11 http://security.ubuntu.com/ubuntu noble-security/main amd64 Packages [617 kB]
Get:12 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Packages [865 kB]
Get:13 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Components [151 kB]
Get:14 http://in.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Components [212 B]       
Get:15 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Packages [1,014 kB]
Get:16 http://security.ubuntu.com/ubuntu noble-security/main amd64 Components [8,956 B]    
Get:17 http://security.ubuntu.com/ubuntu noble-security/restricted amd64 Components [212 B]
Get:18 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Packages [803 kB]
Get:19 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Components [363 kB]          
Get:20 http://in.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Components [940 B]       
Get:21 http://in.archive.ubuntu.com/ubuntu noble-backports/main amd64 Components [208 B]
Get:22 http://in.archive.ubuntu.com/ubuntu noble-backports/restricted amd64 Components [216 B]
Get:23 http://in.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Components [17.7 kB]
Get:24 http://in.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Components [212 B]                
Get:25 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Components [51.9 kB]                   
Get:26 http://security.ubuntu.com/ubuntu noble-security/multiverse amd64 Components [212 B]
Fetched 4,276 kB in 6s (707 kB/s)                                                                                                                                                                          
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
56 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libpq5
Suggested packages:
  postgresql-doc-16
The following NEW packages will be installed:
  libpq-dev libpq5
0 upgraded, 2 newly installed, 0 to remove and 56 not upgraded.
Need to get 292 kB of archives.
After this operation, 1,031 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpq5 amd64 16.6-0ubuntu0.24.04.1 [141 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpq-dev amd64 16.6-0ubuntu0.24.04.1 [151 kB]
Fetched 292 kB in 3s (84.4 kB/s)   
Selecting previously unselected package libpq5:amd64.
(Reading database ... 236928 files and directories currently installed.)
Preparing to unpack .../libpq5_16.6-0ubuntu0.24.04.1_amd64.deb ...
Unpacking libpq5:amd64 (16.6-0ubuntu0.24.04.1) ...
Selecting previously unselected package libpq-dev.
Preparing to unpack .../libpq-dev_16.6-0ubuntu0.24.04.1_amd64.deb ...
Unpacking libpq-dev (16.6-0ubuntu0.24.04.1) ...
Setting up libpq5:amd64 (16.6-0ubuntu0.24.04.1) ...
Setting up libpq-dev (16.6-0ubuntu0.24.04.1) ...
Processing triggers for libc-bin (2.39-0ubuntu8.3) ...
Processing triggers for man-db (2.12.0-4build2) ...
```

Command Executed

```sh
sudo apt install python3.12-dev
```
Output

```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install python3.12-dev
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3.12-dev is already the newest version (3.12.3-1ubuntu0.4).
python3.12-dev set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 56 not upgraded.
```

Install Required Python Packages:
```sh
pip install -r requirements.txt
```
Output:

```sh


(venv) adarsh@adarsh:~/Flask_postgres_valkey$ pip install -r requirements.txt
Collecting Flask==3.1.0 (from -r requirements.txt (line 1))
  Using cached flask-3.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting psycopg2==2.9.10 (from -r requirements.txt (line 2))
  Using cached psycopg2-2.9.10.tar.gz (385 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting redis==5.2.1 (from -r requirements.txt (line 3))
  Using cached redis-5.2.1-py3-none-any.whl.metadata (9.1 kB)
Collecting psycopg2-binary==2.9.10 (from -r requirements.txt (line 4))
  Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
Collecting Werkzeug>=3.1 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting Jinja2>=3.1.2 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting blinker>=1.9 (from Flask==3.1.0->-r requirements.txt (line 1))
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->Flask==3.1.0->-r requirements.txt (line 1))
  Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
Using cached flask-3.1.0-py3-none-any.whl (102 kB)
Using cached redis-5.2.1-py3-none-any.whl (261 kB)
Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached click-8.1.8-py3-none-any.whl (98 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.5-py3-none-any.whl (134 kB)
Using cached werkzeug-3.1.3-py3-none-any.whl (224 kB)
Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23 kB)
Building wheels for collected packages: psycopg2
  Building wheel for psycopg2 (pyproject.toml) ... done
  Created wheel for psycopg2: filename=psycopg2-2.9.10-cp312-cp312-linux_x86_64.whl size=529585 sha256=03fc69a13250eddcf4abcdd4ee00b1aca36871d040d0f8df667f7ca54c4acc21
  Stored in directory: /home/adarsh/.cache/pip/wheels/ac/bb/ce/afa589c50b6004d3a06fc691e71bd09c9bd5f01e5921e5329b
Successfully built psycopg2
Installing collected packages: redis, psycopg2-binary, psycopg2, MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, Flask
Successfully installed Flask-3.1.0 Jinja2-3.1.5 MarkupSafe-3.0.2 Werkzeug-3.1.3 blinker-1.9.0 click-8.1.8 itsdangerous-2.2.0 psycopg2-2.9.10 psycopg2-binary-2.9.10 redis-5.2.1

```
Verify Flask Installation:
```sh
python3 -m flask --version
```
---

### **STEP 3: Start the Containers**

Command executed:
```sh
sudo apt install podman-compose
```

Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ sudo apt install podman-compose
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-dotenv
The following NEW packages will be installed:
  podman-compose python3-dotenv
0 upgraded, 2 newly installed, 0 to remove and 56 not upgraded.
Need to get 60.9 kB of archives.
After this operation, 305 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 python3-dotenv all 1.0.1-1 [22.3 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 podman-compose all 1.0.6-1 [38.6 kB]
Fetched 60.9 kB in 2s (35.6 kB/s)        
Selecting previously unselected package python3-dotenv.
(Reading database ... 237341 files and directories currently installed.)
Preparing to unpack .../python3-dotenv_1.0.1-1_all.deb ...
Unpacking python3-dotenv (1.0.1-1) ...
Selecting previously unselected package podman-compose.
Preparing to unpack .../podman-compose_1.0.6-1_all.deb ...
Unpacking podman-compose (1.0.6-1) ...
Setting up python3-dotenv (1.0.1-1) ...
Setting up podman-compose (1.0.6-1) ...
Processing triggers for man-db (2.12.0-4build2) ...


```
---

### **STEP 4: Run the Containers**

Command executed for PostgreSQL:
```sh
podman run -d --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=employee -p 5432:5432 docker.io/library/postgres
```
Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ podman run -d --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root -e POSTGRES_DB=employee -p 5432:5432 docker.io/library/postgres
Trying to pull docker.io/library/postgres:latest...
Getting image source signatures
Copying blob 4553993e7797 done   | 
Copying blob 0dc773e0cc79 done   | 
Copying blob e1ad38ab49c1 done   | 
Copying blob 20f2363da6db done   | 
Copying blob c29f5b76f736 done   | 
Copying blob 559c5c599163 done   | 
Copying blob 91393204ae54 done   | 
Copying blob c0311d3bf51b done   | 
Copying blob 931e444b6b99 done   | 
Copying blob 0de06291fc41 done   | 
Copying blob 1f9512881cf4 done   | 
Copying blob a608baae1e5c done   | 
Copying blob 91befecb86a3 done   | 
Copying blob 8da49c2b3211 done   | 
Copying config d14b06b9a9 done   | 
Writing manifest to image destination
6d2e74dd33bb6ae90e85307e7340766c9386aba58e097e40bd945bc161fb6441
```

Command executed for Valkey:
```sh 
podman run -d --name valkey_container -p 6379:6379 docker.io/valkey/valkey
```
Output:
```sh
(venv) adarsh@adarsh:~/Flask_postgres_valkey$ podman run -d --name valkey_container -p 6379:6379 docker.io/valkey/valkey
Trying to pull docker.io/valkey/valkey:latest...
Getting image source signatures
Copying blob c29f5b76f736 skipped: already exists  
Copying blob 4f4fb700ef54 done   | 
Copying blob e9c0e091ec2b done   | 
Copying blob 76d6b73e18e0 done   | 
Copying blob f644cba9db5c done   | 
Copying blob a0a0665da571 done   | 
Copying blob f2bf47372ada done   | 
Copying config df4420e738 done   | 
Writing manifest to image destination
1c89e30b37a9e8bcfa651d4a7dbb1128fd617c5b68f6627eac4e98f8faedc19b
```

Verify PostgreSQL is running:
```sh
podman exec -it postgres_container bash
psql -U postgres
```
---

### **STEP 5: Run the Application**

Command executed:
```sh
python app.py
```