Bulletin Board Bot
==================

Bulletin board written in Python using the Aiogram library 🐍

Technical requirements
----------------------

#. At the command **/start** bot sends a welcome message with basic commands, 
   including **/help** to see a complete list of commands. 

#. The bot has a command **/browseAds**, which sends messages with inline browse 
   buttons with which the user switches between ads.

#. Between the browse buttons in the middle there is a button to add the current 
   ad to favorites.

#. Ads may or may not contain photos.

#. The bot has a command **/newAd**, which allows you to add a new ad.

#. After running this command the bot sends a new message that requests you 
   to write a text of an ad and attach pictures if it is needed; the user 
   needs to send the message created by user.

#. The message sent by the bot contains an inline button to cancel adding an ad.

#. The bot has a command **/myAds**, which shows ads added by the user, 
   similar to how the command **/browseAds** shows them, but in addition to those 
   buttons is added a button to edit and delete the current ad.

#. When you click on the delete button, the bot will ask you to confirm this 
   operation using the inline button of message, which contains the front of the ad.
   
#. When you click on the edit button, the bot will ask you to send a message with 
   new text; then the bot will send pictures attached to the old ad, depending on whether 
   you want to change the pictures, you should click on the corresponding inline button; 
   if you decide to change the pictures, the bot will ask you to send new; after all operations, 
   the ad is edited; editing can be canceled at any stage.
   

🏃 How do I run it?
----------------
#. Clone this repository 🚀

    ::

        git clone https://github.com/t3m8ch/bulletin-board-bot.git
        cd bulletin-board-bot

#. Copy **.example.env** to **.env** 🔄

    ::

        cp .example.env .env

#. Edit the **.env** file using a text editor ⚙

    **Required parameters:**
    ::
        TG_TOKEN=Insert_the_telegram_bot_token_here_without_spaces
        ADMINS_ID=List_the_id_of_the_administrators,separated_by_commas_without_spaces

    To use webhook, you only need to specify the environment variable **WEBHOOK_HOST**.
    If this parameter is not specified, long polling is used.

    **Default parameters values:**
    ::

        TG_WEBHOOK_PATH=/bot
        WEBAPP_HOST=localhost
        WEBAPP_PORT=3000
        LOG_LEVEL=info
        DB_CONNECTION_STR=postgresql+asyncpg://localhost/bulletin_board_board

    **All parameters:**
    ::

        TG_TOKEN=Insert_the_telegram_bot_token_here_without_spaces
        TG_ADMINS_ID=List_the_id_of_the_administrators,separated_by_commas_without_spaces
        TG_WEBHOOK_HOST=Insert/the/host/that/will/be/accessed/by/Telegram
        TG_WEBHOOK_PATH=Insert/the/path/to/bot/that/will/be/accessed/by/Telegram

        WEBAPP_HOST=Insert.web.application.host
        WEBAPP_PORT=Insert_web_application_port

        LOG_LEVEL=info

        DB_CONNECTION_STR=insert://connection:string@to/postgres_here


    Valid **LOG_LEVEL** values: **DEBUG**, **INFO**, **WARNING**, **ERROR** and other,
    which are included by default in the python logging library.
    This value of this parameter is case-insensitive.

    **ADMINS_ID** value is considered valid if they are IDs listed,
    separated by commas without spaces.

#. Copy **alembic.example.ini** to **alembic.ini** 🔄

    ::

        cp alembic.example.ini alembic.ini

#. If you changed the default value of **DB_CONNECTION_STR**,
   change it in **alembic.ini** as well ❗

    ::

        sqlalchemy.url = insert://connection:string@to/postgres_here

#. Install the necessary dependencies with the help of **poetry** 🔽

    ::

        poetry install

#. Create a database in Postgresql 🎩

    ::

        psql -c "create database bulletin_board_board"

    You can change the value of *bulletin_board_board* to any other value
    you specify in the **.env** and **alembic.ini** files

#. Do the migrations 🐦

    ::

        poetry run alembic upgrade head

#. You can insert test data to the database 📋

    ::

        poetry run insert_test_data

#. Now you can run the bot! 🎉

    ::

        poetry run

