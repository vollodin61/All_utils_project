FROM python:3.11.5-alpine3.18
# set work directory
WORKDIR /All_utils_project
# copy project
COPY requirements.txt /All_utils_project
# install dependencies
#RUN python -m pip install poetry==1.7.0
#RUN poetry update
RUN pip install -r requirements.txt
COPY . /All_utils_project
#RUN poetry update
# run app
# CMD ["python", "send.py"]
