FROM python:3.9.9 
RUN pip install pipenv
WORKDIR /app/ 
COPY Pipfile \
     Pipfile.lock \
     manage.py \
     /app/ 
#put this before you put in the rest of your source files or you have to reinstall 
#dependencies everytime a file changes
RUN pipenv sync
COPY ./api /app/api
COPY ./forum_backend /app/forum_backend 
EXPOSE 8000
CMD pipenv run python3 manage.py migrate \
    && pipenv run python3 manage.py runserver 0.0.0.0:8000