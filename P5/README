The project takes a baseline installation of a Linux distribution on a virtual machine and
configures it to host the web applications developed in Project 3. The IP address used to
visit the homepage of the application is 52.27.110.245.

1. IP address of the VM is 52.27.110.245, ssh port is 2200

2. Web application home page address: 52.27.110.245.

3. Configuration steps done:

1). Create a new user named grader and configure ssh
a). useradd grader # add user named grader
b). visudo grader # give grader sudo privilege
b). modified /etc/ssh/sshd_config to disable root remote login, change ssh port to 2200,
enable grader to use password to login

2). update pacakges:
apt-get update
apt-get upgrade

3). configure ufw:
ufw allow 2200
ufw allow http
ufw allow ntp
ufw enable

4). install and configure apache
Configure ServerName in apache .conf file to locolhost
enable apache proxy module by command a2enmod proxy
configure apache reverse proxy: map root path '/' to 'locolhost:8000/'
restart apache service

5). install postgresql

6). install git and clone my repository

4. Reference:
stackoverflow.com
askubuntu.com
stackexchange.com

5. password of grader used for remote login:
graderpw

6. contents of udacity_key.rsa:

-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAu1XR1wB/C8+rsp0Yy05HB+1Nnu9SgbuPtgAN6Rird00D2xuM
4Sztdv6moFUSWG+104QuOsQX7KWVLGV/FlxXE0MR6IkHMbr8x4go8I9K7Sx1BPTf
rjGLYv63mFC7y6ntsosefJ+c84DtlqiK8ZlawmJCTEdiYHJdtHHwTQaFOShTUdXv
kqSZ+hUH9+UBSDTtgZ9SupZCSGgiZqQ4V7JK9oRp4fwkA8rTO5Mw11CuVmTSRiM5
tBilaSFlCCe42GA0Rji8UKA/9HTXQHUPgdCbNSodK+sdhBbpCribOsFKkM9Q9Ef9
7Of9DpahOYCKLB/BUEnhFjJvgUr/e4JNrDb8HQIDAQABAoIBAQCQv/QfLBv+tV1W
6vowhXBvGJaEeymGYrXdjFczSEOdMB4NnFET4JIwAv4fHvzI5rBZGmZaNBDEYwFL
x7UWQw1pLcbVpaOwcmpFhtkTX7UmY9abmNaJE3E/cc/M2nzxFoE7FzHcW7x7jqCG
a/7IRZWSYzgVFodWPKhY+D0UVzhze3lNRFEsdOPpIdVEjlg55QPpdAXnci1jJ3ZJ
65HGoTIg2ycJpwOpEBlz11Tz/0Cvgjloi+xaa2JT1M/WCwWo4xixSjEXr/cMP2eZ
/UWT/C6oCBkO/QxrFq/o2vBGmzhm7cKZezFDdQnX66U3YP3dhiLx99g9YvrIlOvd
X65B2d0lAoGBAOdi8cNQ0Z9E9TXAe5Iztpbgf2B+ZwyL4J5tRmuUxFyD8jGpIKOa
RvwwTVjUru9UJgRFd39/X6aaplL/dgalPoevXz8n/AmIP34iP0h0Nhl4Aw7aa2ne
8y+xBIIh31urdrbJ+ntVBTqovifbH7rzxCnP89yU/CjwrN0MVLsD/ES3AoGBAM9D
SGtIqewxgN9fqOfL6sXBMQQ4RWiyu5bAwHUVs5VUsUAJ6azjnTH8XEpv+pnvCQk1
HSAYfAsziEL7IuNIckETBAC4jEbSQRZmZtZW31+HKDu+5FUSutRndHcUSOGS/OZX
/pTirw+4Yzf41FbO5vyfsMvVJpAINvEL8rHQ3nnLAoGBALrIvLEWhKE1YVzKzPXw
mOyivTB/2V/faqt5OueNaBXmzZQZGyf2Wmcp9sZGqhC4tRetnBFoGSa8oJdPcU9c
BWYyw4iQFnz7Z4XCz6MFbMaSgqVy3FLSjy1okGMcRNoTR/m2gmUc9OOtZBN4Z9za
+vdlz025VvUVk/W9BokRZotxAoGALmj/h15vBj+TfvE5riXgPUXkRvCewjH7hWdF
8THZ059yTUeq9pbFNVMwC08Fy4BWAqTND8nLxOpWIcGAb2pigyXR6KNqbdVY0748
WtR7EjX+kVpOYKpgAX3k+2EkbLZwQNgFXqtfzeJY/UiPq5yK5piPiyUAjJH6U4F8
Z8rAdn8CgYA9EBT8/5d72Pjiwsqs8K2pLcU6Zy3iBRogcUQPVaoz2JTGYW4cWcLR
1Rz5A6hF+UqazhAlo4WAsl4X4PKINP2vW3xV7rodqLYxVwt+0S2rBrpxXttYiq5J
dw6FQQqGCGtqvtVCEbiSp38rUjERD+UGIjoM38QzvcFesorPKaxUDw==
-----END RSA PRIVATE KEY-----