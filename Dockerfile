FROM jjanzic/docker-python3-opencv

RUN mkdir /code
ADD ./ /code/
WORKDIR /code

RUN pip install -r requirements.txt


