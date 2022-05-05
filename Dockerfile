FROM centos:latest
RUN yum install python3  python3-devel   gcc-c++ -y && \
    python3 -m pip install --upgrade --force-reinstall pip && \
    yum install sudo -y && \
    yum install --assumeyes  python3-pip && \
    pip install keras && \
    pip install tensorflow --no-cache-dir  tensorflow && \
    pip install --upgrade pip tensorflow && \
    pip3 install flask && \
    pip3 install joblib && \
    pip3 install sklearn && \
    mkdir  /social_media &&  \
    mkdir /social_media/templates
COPY  svm_social_networ.h5    /social_media
COPY  app.py  /social_media
COPY  myform.html  /social_media/templates
COPY  results.html   /social_media/templates
EXPOSE  6666
WORKDIR  /social_media
CMD export FLASK_APP=app.py
ENTRYPOINT flask  run --host=0.0.0.0    --port=6666