FROM registry.redhat.io/ubi8/python-36
EXPOSE 8080
USER root

#Red Hat Enterprise Server 8 and Oracle Linux 8
RUN curl https://packages.microsoft.com/config/rhel/8/prod.repo > /etc/yum.repos.d/mssql-release.repo
RUN yum remove unixODBC-utf16 unixODBC-utf16-devel #to avoid conflicts
RUN yum remove unixODBC-utf13 unixODBC-utf13-devel #to avoid conflicts
RUN ACCEPT_EULA=Y yum install -y msodbcsql18
RUN ACCEPT_EULA=Y yum install -y mssql-tools18
RUN echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
RUN source ~/.bashrc
RUN yum install -y unixODBC-devel

RUN yum install -y vim
WORKDIR /usr/src/app
COPY . .
RUN pip install gunicorn
RUN pip install --no-cache-dir -r requeriments.txt
CMD ["python","manage.py","runserver","0:8080"]
