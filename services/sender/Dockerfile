FROM python:3.11.5-alpine3.18
# set work directory
WORKDIR /sender
# copy project
COPY . /sender
# install dependencies
#RUN python -m pip install poetry==1.7.0
#RUN poetry update
RUN pip install -r requirements.txt
#RUN poetry update
# run app
# CMD ["python", "send.py"]