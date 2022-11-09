FROM huggingface/transformers-pytorch-gpu:4.23.0

RUN pip install --upgrade pip
RUN pip install transformers==4.23.0 flask flask_api gunicorn pydantic accelerate huggingface_hub>=0.9.0 deepspeed>=0.7.3
RUN pip install git+https://github.com/microsoft/DeepSpeed-MII.git
RUN pip install protobuf==3.20.0 grpcio==1.43.0 grpcio-tools==1.43.0