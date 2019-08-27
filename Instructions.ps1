#if project folder don't mount try  reset share credentials


Set-Location "C:\Users\Administrator\Desktop\Django Projects\"
$ProjectName = "WordPress"
New-Item -Path "C:\Users\Administrator\Desktop\Django Projects\$ProjectName" -Type Directory

Get-ChildItem "C:\Users\Administrator\Desktop\Django Projects\django Files\" | Copy-Item -Destination "C:\Users\Administrator\Desktop\Django Projects\$ProjectName"
Set-Location "C:\Users\Administrator\Desktop\Django Projects\$ProjectName"


#Create a Django project  "REPLACE COMPOSEXAMPLE BY PROJCET NAME"
docker-compose run web django-admin startproject $ProjectName .

#Replace this database section in project files "settings.py"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

docker-compose.exe up
