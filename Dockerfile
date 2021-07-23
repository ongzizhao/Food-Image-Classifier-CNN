<<<<<<< HEAD
FROM continuumio/miniconda3:4.9.2

ARG WORK_DIR="/home/polyaxon"
ARG USER="polyaxon"

WORKDIR $WORK_DIR
USER $USER
#RUN mkdir /app 

#mkdir /app/src && \
#mkdir /app/src/templates

#WORKDIR /app
RUN mkdir -p $WORK_DIR && chown -R 2222:2222 $WORK_DIR && cd $WORK_DIR
RUN mkdir ./src/uploads

# COPY files to container
#COPY src/app.py src/app.py
#COPY src/inference.py src/inference.py
#COPY src/templates/index.html src/templates/index.html
COPY src src
COPY model.h5 model.h5
COPY conda.yml conda.yml


RUN conda env update -f conda.yml -n base && \
    rm conda.yml

# DO NOT remove the following line - it is required for deployment on Tekong
RUN chown -R 1000450000:0 $WORK_DIR



EXPOSE 8000

# Add a line here to run your app
CMD ["gunicorn", "-b", "0.0.0.0:8000", "src.app:app"]
#CMD python -m src.app
=======
FROM continuumio/miniconda3:4.9.2

ARG WORK_DIR="/home/polyaxon"
ARG USER="polyaxon"

WORKDIR $WORK_DIR
USER $USER
#RUN mkdir /app 

#mkdir /app/src && \
#mkdir /app/src/templates

#WORKDIR /app
RUN mkdir -p $WORK_DIR && chown -R 2222:2222 $WORK_DIR && cd $WORK_DIR
RUN mkdir ./src/uploads

# COPY files to container
#COPY src/app.py src/app.py
#COPY src/inference.py src/inference.py
#COPY src/templates/index.html src/templates/index.html
COPY src src
COPY model.h5 model.h5
COPY conda.yml conda.yml


RUN conda env update -f conda.yml -n base && \
    rm conda.yml

# DO NOT remove the following line - it is required for deployment on Tekong
RUN chown -R 1000450000:0 $WORK_DIR



EXPOSE 8000

# Add a line here to run your app
CMD ["gunicorn", "-b", "0.0.0.0:8000", "src.app:app"]
#CMD python -m src.app
>>>>>>> ded3763eb708e26668ea8423aefa836c51d4ed3d
