'''
Author: Mecil Meng
Date: 2022-08-10 14:53:42
LastEditors: Mecil Meng
LastEditTime: 2022-08-10 15:00:47
FilePath: /Full_course/alembic/versions/1162d5d15af6_create_posts_table.py
Description:

Copyright (c) 2022 by JCBEL/JCBLE/MSCI/MOTU, All Rights Reserved.
'''
"""create posts table

Revision ID: 1162d5d15af6
Revises:
Create Date: 2022-08-10 14:53:42.460757

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '1162d5d15af6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
