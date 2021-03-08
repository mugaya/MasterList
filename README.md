# Master List
Web based registry (master list)

## Installation
- Setup virtual env
- Run requirement.txt as ```pip install -r requirements.txt```
- Run the initial setup files as ```python manage.py loaddata ml_setup/fixtures/list_general.csv.json``` for all fixtures

## Deployment
- Test deployment by running ```python manage.py runserver```
- Production deployment by copying scripts/master_list.conf to apache folder and making the necessary changes

## Testing
- Test functinality using the default /admin/ page
- API endpoints can be tested in the tests in ml_api app
- This is a browsable API
- Search functionality is available at /api/v1/search/
- GET, POST, HEAD, OPTIONS functionality is available at /api/v1/facility/
- PUT, PATCH, DELETE functionality is available at /api/v1/facility/:facility_id/ where facility_id is UUID
