libraries:
- pip install psycopg2
- pip install python-dotenv

Before running files, make sure to run this command:

Linux:
`curl --create-dirs -o $HOME/.postgresql/root.crt 'https://cockroachlabs.cloud/clusters/b9905c83-31ac-4fab-9051-e943d80fe13d/cert'`

Windows:
`mkdir -p $env:appdata\postgresql\; Invoke-WebRequest -Uri https://cockroachlabs.cloud/clusters/b9905c83-31ac-4fab-9051-e943d80fe13d/cert -OutFile $env:appdata\postgresql\root.crt`

Mac:
`curl --create-dirs -o $HOME/.postgresql/root.crt 'https://cockroachlabs.cloud/clusters/b9905c83-31ac-4fab-9051-e943d80fe13d/cert'`