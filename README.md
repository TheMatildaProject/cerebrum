# Cerebrum
The Cerebrum performs higher functions like interpreting touch, vision and hearing, as well as speech, reasoning, emotions, learning, and fine control of movement. It's also the largest part of the brain and is composed of right and left hemispheres. 

And so, this is a Python app that receives commands and connects Amazon's Lex to process them and hopefully give an appropriate response


## Installation

### Old School
`pip install -r requirements.txt`
`export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>; export AWS_SECRET_KEY_ID=<AWS_SECRET_KEY_ID>; export AWS_REGION_NAME=<AWS_REGION_NAME>; export LEX_BOT_NAME=<LEX_BOT_NAME>; export LEX_BOT_ALIAS=<LEX_BOT_ALIAS>; export LEX_USER_ID=<LEX_USER_ID>; export FLASK_APP=app.py; python app.py -m flask run`

### Docker
#### Build
`docker build --build-arg AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> --build-arg  AWS_SECRET_KEY_ID=<AWS_SECRET_KEY_ID> --build-arg AWS_REGION_NAME<AWS_REGION_NAME> --build-arg  LEX_BOT_NAME=<LEX_BOT_NAME> --build-arg  LEX_BOT_ALIAS=<LEX_BOT_ALIAS> --build-arg LEX_USER_ID=<LEX_USER_ID> . -t cerebrum:latest`

#### One-off run
`docker run -p 5004:5000 --name cerebrum -d cerebrum:latest`