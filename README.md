# finders_keepers
Django project that validates and saves locations.

Live hosted version is available at http://finderskeepers.rowanv.com . 


## Instructions
This app finds locations, and if they have a valid address, it keeps them! To get started, click on a location on the map. If you've chosen a location that has a valid address, you'll see the address saved below the map and a marker will appear at your chosen spot.

## To run application locally
    git clone https://github.com/rowanv/finders_keepers.git
    cd finders_keepers/
    virtualenv --python=python3 YOUR_VIRTUALENV_FOLDER
    YOUR_VIRTUALENV_FOLDER/bin/pip install -r requirements.txt
    YOUR_VIRTUALENV_FOLDER/bin/python3 manage.py migrate
    YOUR_VIRTUALENV_FOLDER/bin/python3 manage.py runserver
    
    
    
## API Keys
This application uses a set of API keys which it presumes are stored in the project directory in a config.yml file. The file should define the following variable: `api_key`: your API key for the Google Maps API. 
    
