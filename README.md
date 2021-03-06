# Udacity Full Stack Web Developer Nanodegree

## Logs Analysis Project

### Project Overview
This project uses Python 3 with psycopg2 as a PostgreSQL adapter to run queries against a fictional news website database. These queries answer:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### Installation Prerequisites
To run these queries, the following programs must be installed:
* Python 3: https://www.python.org/downloads/
* Virtual Box: https://www.virtualbox.org/wiki/Downloads
* Vagrant: https://www.vagrantup.com/downloads.html

### Virtual Machine Configuration
* Download and unzip [Udacity's Vagrant Configuration File](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile).

### Download Data
1. Download and unzip [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
2. Place `newsdata.sql` inside `FSND-Virtual-Machine/vagrant`. This directory can be found in the virtual machine installed in the previous step.

### Clone Repository
* Download/clone this repo and place the resulting `logs-analysis-master` folder inside `FSND-Virtual-Machine/vagrant` as well.

### Start Virtual Machine and Load Data
To run the Vagrant VM and load the news databse, `cd` into the `FSND-Virtual-Machine/vagrant` directory and enter the following commands into your terminal:
* `vagrant up` starts the virtual machine. This may take a few minutes, especially the first time.
* `vagrant ssh` to log into the VM.
* `cd /vagrant`
* Import the data and schema from `newsdata.sql` to the _news_ database by typing `psql -d news -f newsdata.sql`

### Run Queries
* Run the command `python3 logs-analysis-master/logs_analysis.py`.
* The output in your terminal should match included `example_output.txt` file.
