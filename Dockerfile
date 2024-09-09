FROM python:3.12

WORKDIR /crypto

COPY requirements.txt .
COPY run_scripts.sh .
COPY boot.sh .

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x run_scripts.sh
RUN chmod +x boot.sh

COPY . .

CMD ["bash", "./boot.sh"]
