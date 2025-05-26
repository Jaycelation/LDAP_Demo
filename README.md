### LDAP injection

* Challenge 1 - Blind LDAP

* Challenge 2 - LDAP + SSTI

* Challenge 3 - LDAP Privilege Escalation

#### How to build

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jaycelation/LDAP_Demo
   cd web/
    ```

2. **Build docker file**

* Challenge 1
    ```bash
    cd lightweight/challenge
    docker build -t lightweight .
    docker run -d -p 1337:80 --name web1 lightweight
    ```
* Challenge 2
    ```bash
    cd lightweight-2/challenge
    docker build -t lightweight2 .
    docker run -d -p 1338:80 --name web2 lightweight2
    ```
* Challenge 3
    ```bash
    cd lightweight-3/challenge
    docker build -t lightweight3 .
    docker run -d -p 1339:8080 --name web3 lightweight3
    ```
* Write Up
    ```
    Comming soon ...
    ```