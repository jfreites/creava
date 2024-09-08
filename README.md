## Creave

Patreon clone using Django, Tailwindcss and Stripe, for educational purpose only.

The goal of this project is to learn how to create a full saas application using the latest technologies.

## How this application works?

Two kind of users: creators and mecenas, the first one are able to create free or pay content. The second one will be follow to one or more creators and support them buying a subscription.

## Development

Clone this repo

Activate the virtual env

```
.\venv\Scripts\activate (or source venv/bin/activate on Linux or Mac)
```

Install project dependencies

```
pip install -r requirements.txt
```

Install node dependencies

```
npm install
```

Run the project

```
cd src
python manage.py migrate
python manage.py runserver
```

Assets compiling

```
npx tailwindcss -i .\src\static\src\input.css -o .\src\static\src\output.css --watch
```
