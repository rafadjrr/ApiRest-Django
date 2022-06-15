FROM registry.redhat.io/ubi8/python-36
EXPOSE 8080
USER root
RUN curl https://packages.microsoft.com/config/rhel/8/prod.repo > /etc/yum.repos.d/mssql-release.repo
RUN yum remove unixODBC-utf16 unixODBC-utf16-devel #to avoid conflicts
RUN ACCEPT_EULA=Y yum install -y msodbcsql17
RUN ACCEPT_EULA=Y yum install -y mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN source ~/.bashrc
RUN yum install -y unixODBC-devel
RUN yum install -y vim
WORKDIR /usr/src/app
COPY . .
RUN pip install gunicorn
RUN pip install --no-cache-dir -r requeriments.txt
CMD ["python","manage.py","runserver","0:8080"]
ENV "OPENSHIFT_BUILD_NAME"="pyodbc-27" "OPENSHIFT_BUILD_NAMESPACE"="default" "OPENSHIFT_BUILD_SOURCE"="https://github.com/rafadjrr/ApiRest-Django" "OPENSHIFT_BUILD_REFERENCE"="testdocker" "OPENSHIFT_BUILD_COMMIT"="27cae80356cd058567b6a2a029e000956873d11b"
LABEL "io.openshift.build.commit.author"="rafadjrr \u003c46068766+rafadjrr@users.noreply.github.com\u003e" "io.openshift.build.commit.date"="Tue Jun 14 16:58:32 2022 -0400" "io.openshift.build.commit.id"="27cae80356cd058567b6a2a029e000956873d11b" "io.openshift.build.commit.message"="revert commit rhel 8" "io.openshift.build.commit.ref"="testdocker" "io.openshift.build.name"="pyodbc-27" "io.openshift.build.namespace"="default" "io.openshift.build.source-context-dir"="/" "io.openshift.build.source-location"="https://github.com/rafadjrr/ApiRest-Django"
