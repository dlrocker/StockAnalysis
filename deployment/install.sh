
# Install ansible
yum -y install ansible || { echo "Failure installing ansible"; exit 1; }

# Create ansible inventory definition file
cat > /etc/ansible/hosts << EOF
[hdp]
localhost	ansible_connection=local
EOF

echo "Verifying /etc/ansible/hosts was created with contents"
cat /etc/ansible/hosts || { echo "Failed to create /etc/ansible/hosts"; exit 1; }

echo "Running Ansible playbook to perform HDP VM setup"
ansible-playbook install_hdp_requirements.yml || { echo "Failure performing setup for HDP node"; exit 1; } 

echo "Install the Ambari server"
ansible-playbook install_ambari.yml || { echo "Failure installing the Ambari server"; exit 1; }
