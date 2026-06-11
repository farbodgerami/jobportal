 


FROM python:3.13-slim

RUN pip install pip --upgrade 
 
WORKDIR /app
COPY ./core/r.txt /app
RUN pip install -r r.txt 


COPY ./core /app
EXPOSE 8000 
CMD ["python", "manage.py","runserver","0.0.0.0:8000"]

