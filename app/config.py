'''
Author: Mecil Meng
Date: 2022-07-06 09:56:58
LastEditors: Mecil Meng
LastEditTime: 2022-07-06 10:05:42
FilePath: /Full_course/app/config.py
Description:

Copyright (c) 2022 by JCBEL/JCBLE/MSCI/MOTU, All Rights Reserved.
'''
from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
