FROM python:3.10

COPY . my_site

WORKDIR my_site/stocks_products

RUN pip install --no-cache-dir -r requirements.txt && python manage.py migrate

EXPOSE 81

CMD [ "python", "manage.py", "runserver", "0.0.0.0:81" ]
