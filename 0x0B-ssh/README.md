<h1 align='center'><img src='https://img.icons8.com/nolan/2x/console.png' height="25px" right="0">SSH</h1>
<ul align="center">
  <img src='https://user-images.githubusercontent.com/82726832/163710044-187d8655-fd28-4c63-a663-111bfef5c139.gif'>
</ul>

## Background Context

Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using ssh

## Resources
<ul align="center">
  <a href='SSH essentials'><u>SSH essentials</u></a>
  <a href='SSH Config File'><u>SSH Config File</u></a>
  <a href='Public Key Authentication for SSH'><u>Public Key Authentication for SSH</u></a>
  <a href='How Secure Shell Works'><u>How Secure Shell Works</u></a>
</ul>

## Tasks
### 0. Use a private key
Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.
### 1. Create an SSH key pair
Write a Bash script that creates an RSA key pair.
### 2. Client configuration file
Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.
### 3. Let me in!
Now that you have successfully connected to your server, we would also like to join the party.
Add the SSH public key below to your server so that we can connect using the ubuntu user.
### 4. Client configuration file (w/ Puppet)
Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.
