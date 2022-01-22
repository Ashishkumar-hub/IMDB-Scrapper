# IMDB-Scrapper

## AWS cloud Deployment : 

**STEP 1: Go to AWS Elastic beanstalk create an app. Select python as environment 3.7 or above. IN case of any issues go to browser google chrome > More tools > extension settings and disable all. 
**
![unnamed](https://user-images.githubusercontent.com/55132850/150642839-5a802567-3cb3-4c61-a233-fb9aa880596f.png)

**STEP 2: Go to Code Pipeline and create a pipeline. This is connecting Github to elastic beanstalk. Go next Select Github version 2. **
![cc5843e8-a00d-4b40-8068-43f115108729](https://user-images.githubusercontent.com/55132850/150642849-a8c754b3-32dd-4d1e-8c99-00aa9fbe0844.png)

**STEP 3: Go to connect Github, click on the button install an app, authorize and connect to all repositories.
![63a4f436-7830-4b48-8145-ab066ef177a2](https://user-images.githubusercontent.com/55132850/150642852-0ff42a29-4bff-49d6-a1f6-3b1fc82bf3b5.png)

**STEP 4: Select repository name and branch name as main go next. Skip build stage.**
![fb7be6f7-39bf-423e-8c85-0fdabaf5ff18](https://user-images.githubusercontent.com/55132850/150642886-ee6e1caa-43a4-4922-b569-0db1e7ce6f94.png)

**STEP 5: Under Deploy select AWS Elastic Beanstalk. Click Next and create a pipeline.** 
![de77cf5c-e98e-41c7-a27b-f0bc94200ce1](https://user-images.githubusercontent.com/55132850/150642903-b1e1b156-a01d-4e54-a09f-71b0590f40e7.png)

**RESULT: DEPLOYMENT DONE (BOTH GREEN TICKS AT RHS)**
![1b4931e3-6f27-4aa9-a317-29468e27e7e5](https://user-images.githubusercontent.com/55132850/150643044-102e34ab-204b-4d5e-898a-72565227ca63.png)

**DEPLOYED PROJECT:** [IMDB SCRAPPER](Imdbscraper-env.eba-fc43xzkw.us-east-1.elasticbeanstalk.com) 
