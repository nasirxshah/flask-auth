FROM python:3-alpine
WORKDIR /src
COPY . .
RUN pipenv install
EXPOSE 5000
CMD [ "flask","run","--host","0.0.0.0","--port","5000" ]
