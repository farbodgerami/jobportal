 


FROM python:3.13-slim

RUN pip install pip --upgrade 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./core/r.txt /app
RUN pip install -r requirements.txt 


COPY ./core /app
EXPOSE 8000 

CMD ["daphne", "core.asgi:application","-b","0.0.0.0","-p","8000"]
 