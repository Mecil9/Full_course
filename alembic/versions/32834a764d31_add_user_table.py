'''
Author: Mecil Meng
Date: 2022-08-12 15:01:33
LastEditors: Mecil Meng
LastEditTime: 2022-08-12 15:08:28
FilePath: /Full_course/alembic/versions/32834a764d31_add_user_table.py
Description:

Copyright (c) 2022 by JCBEL/JCBLE/MSCI/MOTU, All Rights Reserved.
'''
"""add user table

Revision ID: 32834a764d31
Revises: 64b753eb359c
Create Date: 2022-08-12 15:01:33.094745

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '32834a764d31'
down_revision = '64b753eb359c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
