Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── virtualenv

# Automated deploy
## on my machine


fab deploy --host=rowan@finderskeepers.rowanv.com

## Then on the actual server, within source for the website

sed "s/SITENAME/finderskeepers.rowanv.com/g" \
    deploy_tools/nginx.template.conf | sudo tee \
    /etc/nginx/sites-available/finderskeepers.rowanv.com

 sudo ln -s ../sites-available/finderskeepers.rowanv.com \
    /etc/nginx/sites-enabled/finderskeepersrowanv.com

sed "s/SITENAME/finderskeepers.rowanv.com/g" \
    deploy_tools/gunicorn-upstart.template.conf | sudo tee \
    /etc/init/gunicorn-finderskeepers.rowanv.com.conf

sudo service nginx reload
sudo start gunicorn-finderskeepersrowanv.com
# or sudo restart gunicorn-finderskeepers.rowanv.com

../virtualenv/bin/python3 finders_keepers/manage.py makemigrations
../virtualenv/bin/python3 finders_keepers/manage.py migrate
../virtualenv/bin/python3 finders_keepers/manage.py flush
#../virtualenv/bin/python3 manage.py shell < populate_script.py


