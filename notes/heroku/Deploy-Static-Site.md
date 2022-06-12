# Deploying HTML on Heruko using Heroku CLI


## Steps
1. Register a free account on [Github](https://github.com/signup)
2. Create a new (**private**) repository on Github
3. Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
4. Push your created files on the said repository
5. Register a free account on [Heroku](https://signup.heroku.com/login)
6. Create a new a app on Heroku
   > Look for the `New` dropdown in the top-right corner and click it, then click on **Create new app**. Select a region and give your application a name. The name that you assign here will become the subdomain of your application for public access.
7. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli)
   
   or you can follow this:
   ```bash
   dev@dev:~$ curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
   dev@dev:~$ heroku --version
   heroku/7.60.2 linux-x64 node-v14.19.0
   ```
8. Create files in Github repo

   a. `composer.json`
   You just need the simple entry of **{}**.
   ```json
      {}
   ```

   b. `index.php`
   ```php
      <?php include_once("index.html"); ?>
   ```

   c. `index.html`
   This is the core of your web page and it will contain the HTML content that you want to show/display on your Heroku application.
9. Deploy your code

   #### For an Existing App
   Add a remote to your local repository with the `heroku git:remote` command.
   ```bash
   # set git remote heroku to https://git.heroku.com/example-app.git
   dev@dev:~$ heroku git:remote -a example-app
   ```

   #### Confirming that a remote named `heroku` has been set for your app
   ```bash
   dev@dev:~$ git remote -v
   heroku  https://git.heroku.com/example-app.git (fetch)
   heroku  https://git.heroku.com/example-app.git (push)
   ```

   #### Rename a remote
   ```bash
   dev@dev:~$ git remote rename heroku heroku-staging
   ```

   #### Deploying your code
   ```bash
   dev@dev:~$ git push heroku master
   ```