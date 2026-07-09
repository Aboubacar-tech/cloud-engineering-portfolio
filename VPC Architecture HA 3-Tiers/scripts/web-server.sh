 #!/bin/bash

            yum update -y

            # Installation Apache + Git

            yum install httpd git -y

            # Démarrage Apache

            systemctl start httpd

            systemctl enable httpd

            # Déploiement application

            cd /var/www/html

            rm -rf *

            git clone https://github.com/Aboubacar-tech/portfolio.git .

            # Permissions

            chown -R apache:apache /var/www/html

            systemctl restart httpd