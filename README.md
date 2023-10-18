# ZCODERZ (HAKI ) :).

#### HOW TO SETUP ON LOCAL Development:

you need to install python =>3.10

#### create new env:

```shell
         # Create the project directory
        mkdir newDir
        cd newDir
        
        # Create a virtual environment to isolate our package dependencies locally
        python3 -m venv env
        source env/bin/activate  # On Windows use `env\Scripts\activate`
        
        # Install requirements into the virtual environment
        pip install -r requirements.txt
        python3 manage.py makemigrations
        python3 manage.py migrate
        
        
```

create new file with the name  **.env file:**
and make sure to have all things critical in it

## Run the server

`python3 manage.py runserver`

If you want to create a new superuser in order to use the Django admin, you can do the following:

Run  `python3 scripts/manage.py shell`
Execute the following code:

```python

from haki_backend.apps.users.config.services import user_create_superuser

user_create_superuser(
    email='your_email@here.com',
    password='password-that-you-are-going-to-use-to-access-the-admin'
)
```

You now have a new superuser! You can navigate to `http://127.0.0.1:8000/admin/` in order to use the Django admin.

-----
# Response class 
This class unifies the responses for all the apis

Where every response should contain:

- data
- status
- message
- success
- pagination info ( if you enable pagination )

* If you want to paginate data you must call ```response.paginate( request, data)```, then
call ```response.collect(status, message, data, is_paginte)```

  - status: ```it's value is ( 200, 400, 401, 404, 500, ... ) it's default value is 200```.
  - status: ```*string``` describe response ```it's default value empty```.
  - data: ```*array``` express the data you want to send with response 
  ```default value is [] if you call response.paginate before response.collect```<br/> 
   the data will be stored in the response instance automatically after the pagination process   
  - is_paginated: ```*boolean``` if you want to show pagination data in the response, just send ```is_pagination=true default value is false```
#### Example:
```python
    self.response.paginate(request, serialized_data)
    return self.response.collect({"status": status.HTTP_200_OK}, is_paginated=True)
```

* if you don't have data || you don't  want to paginate data just call ```response.collect(status, message)```
#### Example:
```python 
     return self.response.collect({'message': "", "status": })
```
  
-----