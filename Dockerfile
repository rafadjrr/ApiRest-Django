FROM registry.redhat.io/ubi8/python-36
WORKDIR /usr/src/app
EXPOSE 8080
COPY requeriments.txt ./
USER root
RUN yum install -y vim
RUN pip install gunicorn
RUN pip install --no-cache-dir -r requeriments.txt
COPY . .
CMD ["python","manage.py","runserver","0:8080"]
ENV "OPENSHIFT_BUILD_NAME"="djangorest-6" "OPENSHIFT_BUILD_NAMESPACE"="default" "OPENSHIFT_BUILD_SOURCE"="https://github.com/rafadjrr/ApiRest-Django" "OPENSHIFT_BUILD_REFERENCE"="develop" "OPENSHIFT_BUILD_COMMIT"="01fbbdd05d2fa3ba9a74010d29bd38b0be7f607e"
LABEL "io.openshift.build.commit.author"="Rafael \u003crafadjrr@gmail.com\u003e" "io.openshift.build.commit.date"="Mon Mar 7 17:14:26 2022 -0400" "io.openshift.build.commit.id"="01fbbdd05d2fa3ba9a74010d29bd38b0be7f607e" "io.openshift.build.commit.message"="install vim" "io.openshift.build.commit.ref"="develop" "io.openshift.build.name"="djangorest-6" "io.openshift.build.namespace"="default" "io.openshift.build.source-context-dir"="/" "io.openshift.build.source-location"="https://github.com/rafadjrr/ApiRest-Django"
