FROM registry.redhat.io/ubi8/python-36

EXPOSE 8080

USER root
RUN curl https://packages.microsoft.com/config/rhel/8/prod.repo > /etc/yum.repos.d/mssql-release.repo
#RUN yum remove unixODBC-utf16 unixODBC-utf16-devel
RUN yum install -y unixODBC-devel
RUN yum install -y vim

WORKDIR /usr/src/app
COPY . .
RUN pip install gunicorn
RUN pip install --no-cache-dir -r requeriments.txt

CMD ["python","manage.py","runserver","0:8080"]
#ENV "OPENSHIFT_BUILD_NAME"="djangorest-6" "OPENSHIFT_BUILD_NAMESPACE"="default" "OPENSHIFT_BUILD_SOURCE"="https://github.com/rafadjrr/ApiRest-Django" "OPENSHIFT_BUILD_REFERENCE"="develop" "OPENSHIFT_BUILD_COMMIT"="01fbbdd05d2fa3ba9a74010d29bd38b0be7f607e"
#LABEL "io.openshift.build.commit.author"="Rafael \u003crafadjrr@gmail.com\u003e" "io.openshift.build.commit.date"="Mon Mar 7 17:14:26 2022 -0400" "io.openshift.build.commit.id"="01fbbdd05d2fa3ba9a74010d29bd38b0be7f607e" "io.openshift.build.commit.message"="install vim" "io.openshift.build.commit.ref"="develop" "io.openshift.build.name"="djangorest-6" "io.openshift.build.namespace"="default" "io.openshift.build.source-context-dir"="/" "io.openshift.build.source-location"="https://github.com/rafadjrr/ApiRest-Django"
#ENV "OPENSHIFT_BUILD_NAME"="djangorest-7" "OPENSHIFT_BUILD_NAMESPACE"="default" "OPENSHIFT_BUILD_SOURCE"="https://github.com/rafadjrr/ApiRest-Django" "OPENSHIFT_BUILD_REFERENCE"="develop" "OPENSHIFT_BUILD_COMMIT"="eb8395d67e3175e9dacbf52d355826db9895e995"
#LABEL "io.openshift.build.commit.author"="Rafael Rodriguez Openshift \u003crafadjrr@gmail.com\u003e" "io.openshift.build.commit.date"="Fri May 27 14:53:10 2022 +0000" "io.openshift.build.commit.id"="eb8395d67e3175e9dacbf52d355826db9895e995" "io.openshift.build.commit.message"="modelo de datos industrial version 1" "io.openshift.build.commit.ref"="develop" "io.openshift.build.name"="djangorest-7" "io.openshift.build.namespace"="default" "io.openshift.build.source-context-dir"="/" "io.openshift.build.source-location"="https://github.com/rafadjrr/ApiRest-Django"
