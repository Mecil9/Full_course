'''
Author: Mecil Meng
Date: 2022-08-12 15:12:41
LastEditors: Mecil Meng
LastEditTime: 2022-08-12 15:15:23
FilePath: /Full_course/alembic/versions/61a616e8905a_add_foreign_key_to_posts_table.py
Description:添加外键

Copyright (c) 2022 by JCBEL/JCBLE/MSCI/MOTU, All Rights Reserved.
'''
"""add foreign-key to posts table

Revision ID: 61a616e8905a
Revises: 32834a764d31
Create Date: 2022-08-12 15:12:41.651707

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '61a616e8905a'
down_revision = '32834a764d31'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk',
                          source_table='posts',
                          referent_table='users',
                          local_cols=['owner_id'],
                          remote_cols=['id'],
                          ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
