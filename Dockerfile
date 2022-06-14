FROM registry.redhat.io/ubi7/python-36
EXPOSE 8080
USER root

# rhel 7
RUN curl https://packages.microsoft.com/config/rhel/7/prod.repo > /etc/yum.repos.d/mssql-release.repo

RUN yum remove unixODBC-utf16 unixODBC-utf16-devel #to avoid conflicts
RUN ACCEPT_EULA=Y yum install msodbcsql
# optional: for bcp and sqlcmd
RUN ACCEPT_EULA=Y yum install mssql-tools
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc
# optional: for unixODBC development headers
RUN yum install unixODBC-devel


RUN yum install -y vim
WORKDIR /usr/src/app
COPY . .
RUN pip install gunicorn
RUN pip install --no-cache-dir -r requeriments.txt
CMD ["python","manage.py","runserver","0:8080"]
