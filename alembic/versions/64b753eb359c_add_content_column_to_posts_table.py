'''
Author: Mecil Meng
Date: 2022-08-12 14:51:42
LastEditors: Mecil Meng
LastEditTime: 2022-08-12 14:52:41
FilePath: /Full_course/alembic/versions/64b753eb359c_add_content_column_to_posts_table.py
Description:

Copyright (c) 2022 by JCBEL/JCBLE/MSCI/MOTU, All Rights Reserved.
'''
"""add content column to posts table

Revision ID: 64b753eb359c
Revises: 1162d5d15af6
Create Date: 2022-08-12 14:51:42.089096

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '64b753eb359c'
down_revision = '1162d5d15af6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
