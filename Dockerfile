FROM registry.redhat.io/ubi8/python-36
EXPOSE 8080
USER root
RUN curl https://packages.microsoft.com/config/rhel/8/prod.repo > /etc/yum.repos.d/mssql-release.repo
RUN yum install -y unixODBC-devel
RUN yum install -y vim
WORKDIR /usr/src/app
COPY . .
RUN pip install gunicorn
RUN pip install --no-cache-dir -r requeriments.txt
CMD ["python","manage.py","runserver","0:8080"]
ENV "OPENSHIFT_BUILD_NAME"="pyodbc-10" "OPENSHIFT_BUILD_NAMESPACE"="default" "OPENSHIFT_BUILD_SOURCE"="https://github.com/rafadjrr/ApiRest-Django" "OPENSHIFT_BUILD_REFERENCE"="testdocker" "OPENSHIFT_BUILD_COMMIT"="5abcb1ff0435e9fabf07c54e69fa39d3ad0fd6eb"
LABEL "io.openshift.build.commit.author"="rafadjrr \u003c46068766+rafadjrr@users.noreply.github.com\u003e" "io.openshift.build.commit.date"="Tue Jun 14 13:35:44 2022 -0400" "io.openshift.build.commit.id"="5abcb1ff0435e9fabf07c54e69fa39d3ad0fd6eb" "io.openshift.build.commit.message"="test para resolver unixdbc no encontrado" "io.openshift.build.commit.ref"="testdocker" "io.openshift.build.name"="pyodbc-10" "io.openshift.build.namespace"="default" "io.openshift.build.source-context-dir"="/" "io.openshift.build.source-location"="https://github.com/rafadjrr/ApiRest-Django"
