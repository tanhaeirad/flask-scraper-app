FROM python:3.9.1

RUN cd /tmp
RUN apt update

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb

RUN wget https://chromedriver.storage.googleapis.com/111.0.5563.64/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/bin/chromedriver


WORKDIR /app

COPY requirements.txt .

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["bash"]